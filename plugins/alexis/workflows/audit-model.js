export const meta = {
  name: 'audit-model',
  description: 'Audit a data model at scale: one reviewer per table or SQL/DAX file, each finding adversarially verified by a second agent, then one ranked report. Pass args: { target: "sql/" } or a list of paths.',
  phases: ['Discover', 'Review', 'Verify', 'Report'],
}

// args: a path string, an array of paths, or { target, focus }.
const target = typeof args === 'string' ? args : (args && args.target) || (Array.isArray(args) ? null : '.')
const focus = (args && args.focus) || 'correctness (grain, keys, join cardinality, NULL handling), performance, naming and documentation'

phase('Discover')
const found = Array.isArray(args)
  ? { files: args }
  : await agent(
      `List the data model files under ${target}: SQL models (.sql), PySpark transformations (.py under src/ or pipelines/), dbt models, and Power BI model files (.tmdl). ` +
      'Skip tests, generated files, virtualenvs and anything under results/ or outputs/. Return at most 60 paths, most important first (gold before silver before bronze).',
      {
        label: 'discover',
        effort: 'low',
        schema: {
          type: 'object',
          required: ['files'],
          properties: { files: { type: 'array', items: { type: 'string' } } },
        },
      },
    )

log(`Reviewing ${found.files.length} files`)

const findingSchema = {
  type: 'object',
  required: ['file', 'findings'],
  properties: {
    file: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['severity', 'location', 'problem', 'fix'],
        properties: {
          severity: { type: 'string', enum: ['critical', 'important', 'minor'] },
          location: { type: 'string' },
          problem: { type: 'string' },
          fix: { type: 'string' },
        },
      },
    },
  },
}

const verdictSchema = {
  type: 'object',
  required: ['confirmed'],
  properties: {
    confirmed: {
      type: 'array',
      items: {
        type: 'object',
        required: ['severity', 'location', 'problem', 'fix', 'evidence'],
        properties: {
          severity: { type: 'string', enum: ['critical', 'important', 'minor'] },
          location: { type: 'string' },
          problem: { type: 'string' },
          fix: { type: 'string' },
          evidence: { type: 'string' },
        },
      },
    },
  },
}

const reviewed = await pipeline(
  found.files,
  file =>
    agent(
      `Review ${file} for: ${focus}. Read the file and whatever it depends on. ` +
      'Report only real problems with a concrete location (file:line or object name) and a concrete fix. ' +
      'Read-only: do not modify any file and do not run queries that write.',
      { label: `review ${file}`, phase: 'Review', agentType: 'alexis:sql-reviewer', schema: findingSchema },
    ),
  review =>
    review && review.findings.length
      ? agent(
          `You are a skeptical second reviewer. For each finding below, re-read the code and keep it only if it is real and the fix is correct. ` +
          `Drop false positives and style opinions. Add the evidence (the exact code) for each finding you keep.\n\n${JSON.stringify(review)}`,
          { label: `verify ${review.file}`, phase: 'Verify', schema: verdictSchema },
        ).then(v => ({ file: review.file, findings: v ? v.confirmed : [] }))
      : { file: review ? review.file : 'unknown', findings: [] },
)

phase('Report')
const results = reviewed.filter(Boolean)
const total = results.reduce((n, r) => n + r.findings.length, 0)
log(`${total} confirmed findings across ${results.length} files`)

const report = await agent(
  'Write a concise audit report in Markdown from these verified findings. Start with one sentence: the overall verdict and the number of critical findings. ' +
  'Then a table: severity, file, location, problem, fix, sorted critical first. End with the 3 changes that would most reduce risk. ' +
  `Reply in the language the user has been using.\n\n${JSON.stringify(results)}`,
  { label: 'report', effort: 'medium' },
)

return report
