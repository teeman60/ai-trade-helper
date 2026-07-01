## ai-trade-helper
a tool to help traders use AI in making better trading decisions

# Volatility-First Trading System (Institutional-Grade Skeleton)

## Overview
This is a modular trading system that:
- Prioritizes volatility regime analysis (IV, RV, IV rank)
- Incorporates liquidity sweeps, market structure, and FVG
- Maps equity signals into options contracts
- Includes backtesting + paper trading scaffolding

## ⚠️ IMPORTANT
This is NOT a profitable system out of the box.
It is a research + engineering framework.

---

## Required Data Subscriptions (PLACEHOLDERS)

You must choose ONE market data provider:

### Option A (Recommended)
- Polygon.io (stocks + options + IV)
  https://polygon.io

### Option B
- Interactive Brokers (IBKR)
  https://interactivebrokers.com

### Option C
- Alpaca (free tier, limited options)
  https://alpaca.markets

---

## Optional Enhancements (Institutional Level)
- ORATS (options analytics + IV surface)
- Tradier (options chain API)
- CBOE data (volatility indices)
- Bloomberg (enterprise only)

---

## Core Concepts Implemented
- IV Percentile / Rank
- Realized Volatility
- IV / RV ratio
- Volatility Regime Classification
- Market Structure (HH/HL, BOS)
- Liquidity Sweeps
- FVG detection
- Options contract scoring
- Backtesting engine (event-driven skeleton)

---

## Python / Package Manager
This project now uses **Python 3.11+** and **Poetry** for dependency management.

### Recommended workflow (Poetry)
```bash
cd /Users/teewhy/Desktop/ai-trade-helper
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
pyenv local 3.11.12
python -m pip install --upgrade pip
python -m pip install --user poetry
poetry install
poetry run python main.py
```

### Alternative: pip + venv
If you prefer a lightweight local environment, use this approach instead:
```bash
cd /Users/teewhy/Desktop/ai-trade-helper
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

> If you use Poetry, make sure VS Code is pointed to the Poetry-created venv in `.venv`.

---

## Notes
- `scipy` requires Python 3.11+ in this repo.
- The current Poetry config uses `package-mode = false`, so the project is dependency-managed only.
- If you want CI compatibility, `requirements.txt` contains pinned versions for pip installs.

---

## Architecture

Data → Vol Engine → Structure Engine → Setup Engine → Options Engine → Backtester → Alerts
