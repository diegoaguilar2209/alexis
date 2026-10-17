export const meta = {
  name: 'migrate',
  description: 'Migrate many files in parallel with verification: one agent per file in its own worktree, then a checker per file and a final summary. Pass args: { instruction: "convert to PySpark 4 APIs", target: "src/", check: "pytest -q" }.',
  phases: ['Plan', 'Migrate', 'Check', 'Summary'],
}

if (!args || !args.instruction) {
  throw new Error('migrate needs args.instruction, e.g. { instruction: "replace pandas with polars", target: "src/", check: "pytest -q" }')
}
const instruction = args.instruction
const target = args.target || '.'
const check = args.check || 'the project verification command from CLAUDE.md'

phase('Plan')
const plan = await agent(
  `We will apply this migration: "${instruction}". List every file under ${target} that needs the change. ` +
  'Exclude generated files and virtualenvs. Also return a short list of rules every file must follow so results are consistent.',
  {
    label: 'plan',
    schema: {
      type: 'object',
      required: ['files', 'rules'],
      properties: {
        files: { type: 'array', items: { type: 'string' } },
        rules: { type: 'array', items: { type: 'string' } },
      },
    },
  },
)

log(`Migrating ${plan.files.length} files`)
const rules = plan.rules.map(r => `- ${r}`).join('\n')

const results = await pipeline(
  plan.files,
  file =>
    agent(
      `Apply this migration to ${file} only: "${instruction}".\nRules:\n${rules}\n` +
      `Then run ${check} for what this file affects, fix what you broke, and commit with message "refactor: ${instruction} in ${file}". ` +
      'Do not weaken or skip tests. Return the commit hash, or explain why the file could not be migrated.',
      { label: `migrate ${file}`, phase: 'Migrate', isolation: 'worktree' },
    ),
  (outcome, file) =>
    agent(
      `Check the migration of ${file} ("${instruction}") as an independent reviewer. Outcome reported by the migrating agent:\n${outcome}\n` +
      'Verify the rules were followed and nothing outside the migration changed. Reply with PASS or FAIL and one line of reason.',
      { label: `check ${file}`, phase: 'Check', effort: 'low' },
    ).then(verdict => ({ file, outcome, verdict })),
)

phase('Summary')
return await agent(
  'Summarize this migration for the user in Markdown: how many files passed, a table of files that failed with the reason, and the exact next step for each failure. ' +
  `Remind them each passing file was committed on its own worktree branch and needs merging.\n\n${JSON.stringify(results.filter(Boolean))}`,
  { label: 'summary', effort: 'low' },
)
