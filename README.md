# Monte Carlo Retirement Simulation

This is a Python rebuild of a retirement-planning simulation I worked on during graduate analytics coursework. I wanted the assumptions and scenario logic to be visible in code instead of living only inside a spreadsheet or class submission.

The question is simple: **how does annual contribution level change the chance of reaching a $1,000,000 portfolio after 20 years?**

## Assumptions

For the current version I use:

- starting balance: **$50,000**
- expected annual return: **7%**
- annual volatility: **12%**
- time horizon: **20 years**
- simulations per scenario: **10,000**
- annual contribution scenarios: **$12K, $18K, $24K, $30K**

Returns are sampled independently from a normal distribution and clipped so a simulated annual loss cannot fall below -95%.

## Results

| Annual contribution | Median ending balance | Probability of reaching $1M |
|---:|---:|---:|
| $12,000 | $636,334 | 11.3% |
| $18,000 | $869,146 | 34.3% |
| $24,000 | $1,100,038 | 61.2% |
| $30,000 | $1,332,135 | 80.3% |

The result I find most useful is the change between scenarios rather than any single projected ending balance. Under these assumptions, moving from $18K to $24K in annual contributions shifts the probability of reaching the target from about one-third to above 60%.

## Why Monte Carlo instead of one forecast

A single compound-growth calculation gives one path. Monte Carlo gives a distribution of possible paths, which makes it easier to talk about uncertainty and downside risk instead of pretending the average return happens every year.

The script also calculates mean, median, 10th-percentile, and 90th-percentile ending balances for each contribution level.

## Run it

```bash
pip install -r requirements.txt
python src/simulation.py
```

To change the number of simulations:

```bash
python src/simulation.py --simulations 50000
```

The scenario summary is written to `results/scenario_summary.csv`.

## Stack

Python · NumPy · pandas · probability · simulation

## Limitations

This is an analytics exercise, not financial advice. The model is intentionally simple: it does not include inflation, taxes, fees, changing contribution levels, asset allocation, correlated returns, or a more realistic return-generating process.

If I extended it, I would add inflation-adjusted targets, multiple return regimes, withdrawal scenarios, and sensitivity analysis around return/volatility assumptions.
