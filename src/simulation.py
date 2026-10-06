from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd


def simulate(starting_balance=50_000, annual_contribution=18_000, years=20,
             expected_return=0.07, volatility=0.12, simulations=10_000, seed=42):
    rng = np.random.default_rng(seed)
    balances = np.full(simulations, float(starting_balance))
    for _ in range(years):
        annual_returns = rng.normal(expected_return, volatility, simulations)
        annual_returns = np.clip(annual_returns, -0.95, None)
        balances = balances * (1 + annual_returns) + annual_contribution
    return balances


def contribution_scenarios(contributions, target=1_000_000, **kwargs):
    rows=[]
    for contribution in contributions:
        balances=simulate(annual_contribution=contribution, **kwargs)
        rows.append({
            'annual_contribution': contribution,
            'median_ending_balance': float(np.median(balances)),
            'mean_ending_balance': float(np.mean(balances)),
            'probability_reaching_target': float(np.mean(balances >= target)),
            'p10_balance': float(np.percentile(balances,10)),
            'p90_balance': float(np.percentile(balances,90)),
        })
    return pd.DataFrame(rows)

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--simulations',type=int,default=10_000)
    args=parser.parse_args()
    out=contribution_scenarios([12_000,18_000,24_000,30_000],simulations=args.simulations)
    Path('results').mkdir(exist_ok=True)
    out.to_csv('results/scenario_summary.csv',index=False)
    print(out.to_string(index=False))
