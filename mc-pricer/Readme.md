# Monte Carlo Option Pricing Engine

This project implements a Monte Carlo simulation engine for pricing
financial derivatives under risk-neutral dynamics.

It is designed to demonstrate:
- probabilistic reasoning
- numerical simulation
- variance reduction
- statistical validation

---

## Mathematical Model

### Risk-Neutral Pricing

The fair price of a derivative is:

E[ exp(-rT) · payoff(S_T) ]

---

### Asset Dynamics (GBM)

We simulate prices using Geometric Brownian Motion:

dS_t = r S_t dt + σ S_t dW_t

Exact solution:

S_T = S_0 · exp((r − 0.5σ²)T + σ√T Z),   Z ~ N(0,1)

---

## Monte Carlo Estimator

Price ≈ (1/N) Σ exp(-rT) · payoff(S_T⁽ⁱ⁾)

Convergence rate: O(1 / √N)

---

## Variance Reduction

### Antithetic Variates
For every random draw Z, also simulate −Z.

### Control Variate
Use Black–Scholes closed-form price as a control.

Adjusted estimator:

X* = X − b(Y − E[Y])
b = Cov(X,Y) / Var(Y)

---

## Statistical Output

- mean: price estimate
- std: payoff variability
- stderr = std / √N
- 95% CI = mean ± 1.96 · stderr

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run example:

python run_example.py

Or via CLI:

python -m mc.cli \
  --s 100 --k 100 --r 0.03 --sigma 0.2 --t 1 \
  --paths 200000 \
  --vr antithetic --vr control_variate
