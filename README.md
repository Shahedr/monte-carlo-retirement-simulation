# Monte Carlo Retirement Simulation

Portfolio recreation of a graduate analytics project using Monte Carlo simulation to evaluate long-term retirement outcomes under uncertainty.

## Question
How does annual contribution level change the probability of reaching a **$1,000,000** portfolio target over 20 years?

## Method
- 10,000 simulations per contribution scenario
- Starting balance: $50,000
- Expected annual return: 7%
- Annual volatility: 12%
- 20-year investment horizon
- Contribution scenarios: $12K, $18K, $24K, $30K per year

## Results
| Annual contribution | Median ending balance | Probability of reaching $1M |
|---:|---:|---:|
| $12,000 | $636,334 | 11.3% |
| $18,000 | $869,146 | 34.3% |
| $24,000 | $1,100,038 | 61.2% |
| $30,000 | $1,332,135 | 80.3% |

## Tools
**Python · NumPy · pandas · Monte Carlo Simulation · Probability · Risk Analysis**

## Repository structure
```text
monte-carlo-retirement-simulation/
├── src/simulation.py
├── results/scenario_summary.csv
├── requirements.txt
└── README.md
```

## Run
```bash
pip install -r requirements.txt
python src/simulation.py
```

## What this demonstrates
Scenario modeling, probability-based decision support, reproducible simulation, percentile-based risk analysis, and communicating uncertainty in business terms.
