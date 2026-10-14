# DAX patterns and anti-patterns

## Formatting
Use variables for every intermediate step and return a single expression. Format with DAX Formatter conventions (one function argument per line when long).

```dax
Revenue YoY % =
VAR CurrentRevenue = [Revenue]
VAR PriorRevenue = [Revenue LY]
RETURN
    DIVIDE ( CurrentRevenue - PriorRevenue, PriorRevenue )
```

## Core patterns

```dax
Revenue = SUM ( Sales[Amount] )

Revenue LY =
CALCULATE ( [Revenue], SAMEPERIODLASTYEAR ( 'Date'[Date] ) )

Revenue YTD =
TOTALYTD ( [Revenue], 'Date'[Date] )

Revenue vs Target % =
DIVIDE ( [Revenue] - [Target], [Target] )

Revenue Share of Total =
DIVIDE ( [Revenue], CALCULATE ( [Revenue], REMOVEFILTERS ( Product ) ) )

Revenue Rolling 3M =
CALCULATE (
    [Revenue],
    DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -3, MONTH )
)
```

## Anti-patterns to flag

| Anti-pattern | Why | Fix |
| --- | --- | --- |
| `a / b` | Errors on zero | `DIVIDE ( a, b )` |
| Calculated column for a ratio or aggregate | Wrong at aggregate level, bloats model | Measure |
| `FILTER ( Sales, Sales[Color] = "Red" )` as CALCULATE filter | Iterates the whole table | `Sales[Color] = "Red"` or `KEEPFILTERS` |
| Nested `SUMX` over large facts | Slow | Pre-aggregate upstream or use a single iterator over a dimension |
| `ALL` everywhere | Removes filters users expect | `REMOVEFILTERS` / `ALLSELECTED` deliberately |
| Time intelligence on fact dates | Gaps break functions | Use the marked date table |
| Repeated logic copied across measures | Diverges over time | Base measure + derived measures |
| `IFERROR` / `ISERROR` | Hides problems, slow | Handle the specific case (`DIVIDE`, `ISBLANK`) |
| Hard-coded years or IDs | Breaks next period | Relative date logic or a parameter table |

## Validation
- Compare totals of a changed measure before and after on the same filter context.
- Test at every grain the report uses (total, year, month, category).
- Check blanks vs zeros intentionally (show zero only when zero is meaningful).
