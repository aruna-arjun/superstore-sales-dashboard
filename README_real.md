# Superstore Sales Intelligence — Data Analytics Portfolio Project

A retail sales analytics project built on the well-known public **"Sample
Superstore"** dataset — the same dataset used in thousands of Power BI/Tableau
tutorials, so it's instantly recognizable to anyone reviewing your portfolio.
This version replaces the earlier synthetic dataset with **real transaction
data**, including a genuine data-cleaning step.

## What's in this project

| File | Purpose |
|---|---|
| `real_superstore.csv` | Raw source file, downloaded from a public GitHub mirror |
| `clean_data.py` | Cleans the raw file — strips out two accidentally-merged extra tables (a region lookup and a returns list) that were appended below the real order data, parses dates, fixes types |
| `superstore_clean.csv` | The cleaned dataset — 9,994 real US orders (2015–2018), 21 columns |
| `analyze_real.py` | Pandas analysis — KPIs, monthly trend, category/sub-category/region/state/product/segment breakdowns |
| `dashboard_data_real.json` | Output of the analysis |
| `dashboard_real.html` | Interactive standalone dashboard — open directly in any browser |

## Why this matters more than the synthetic version

Real datasets are messy. This one had two other tables silently pasted
below row 9,994 of the CSV — a problem you'd absolutely hit in a real job.
Handling that (rather than assuming clean data) is exactly the kind of
judgment call interviewers want to hear about.

## Key insights the dashboard surfaces

- **Total sales**: $2.30M across 9,994 orders, 12.5% overall profit margin
- **The headline finding**: Tables (-$17,725), Bookcases (-$3,473), and
  Supplies (-$1,189) are sold at a **net loss** — despite generating real
  revenue, they lose money once discounts are factored in. Technology and
  Office Supplies, by contrast, are healthy — Technology alone contributes
  over half of total profit.
- **Seasonality**: Q4 (Sep–Nov) is consistently the strongest quarter across
  all four years — useful for staffing and inventory planning
- **Geography**: California and New York alone account for roughly a third
  of total sales — a concentration worth flagging in any regional strategy
  discussion

## How to use it

1. Open `dashboard_real.html` in any browser — fully self-contained
2. To re-run from scratch: `python3 clean_data.py` then `python3 analyze_real.py`

## Suggested resume bullets for this project

**Retail sales & profitability analysis** *(Python, Pandas, Chart.js)*
- Cleaned a real 10,800-row transactional dataset, identifying and removing
  two erroneously merged tables to recover 9,994 valid order records
- Analyzed sales and profit across regions, categories, and time, identifying
  three sub-categories generating negative profit despite positive revenue
- Built an interactive dashboard surfacing seasonal trends, regional
  concentration, and margin risks for non-technical stakeholders

## Suggested next steps to strengthen this further

- Rebuild the same analysis in actual Power BI (since your resume lists
  Power BI) using `superstore_clean.csv` — screenshot it for your portfolio
- Write a one-paragraph recommendation: e.g. "investigate discount policy on
  Tables — average discount is unusually high relative to margin" — this is
  the kind of narrative an analyst is actually hired to produce
- Push this to GitHub with a clear commit history: one commit for the raw
  data, one for the cleaning step, one for the analysis — this alone shows
  process, not just output
