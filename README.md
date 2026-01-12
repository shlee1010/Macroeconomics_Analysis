# Macroeconomic Analysis & Market Intelligence

> **A Quantitative Framework for Monitoring US Economic Cycles and Asset Allocation.** > _Connecting Macroeconomic Data (FRED) to Financial Markets (S&P 500/Nasdaq) using Python._

---

## Projects

Investment decisions should be driven by data, not narratives. The goal of this repository is to build a **Top-Down Macro Analysis Pipeline** that systematically evaluates the health of the US economy and its implications for asset prices.

This project is not a one-time analysis but an **evolving dashboard** that tracks key economic engines:

1.  **Liquidity:** The fuel of the market (Money Supply: M2).
2.  On Progress

Currently, this repository hosts the **Liquidity Module (M2)**, with plans to expand into Yield Curve analysis and Real Rate regimes.

---

## Project Structure (The Hierarchy)

This project follows a **modular design pattern** to ensure scalability and maintainability.

```text
US-Macro-Analysis/
│
├── notebooks/                  # Analysis Modules
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Liquidity_M2_Analysis.ipynb  <-- Current Focus
│   └── 03_Yield_Curve_Study.ipynb      <-- Next Step
│
├── src/                        # Reusable Codebase
│   ├── data_loader.py          # Data ingestion engine
│   └── utils.py                # Helper functions for stats
│
├── images/                     # Visualization Exports
└── README.md                   # Project Documentation
```

---

## Tech Stack & Implementation

This project follows a **modular Object-Oriented Programming (OOP)** design to ensure scalability.

- **Data Pipeline:** Automated fetching from **FRED (Federal Reserve Economic Data)** and **Yahoo Finance**.
- **Core Libraries:** `pandas` (Manipulation), `matplotlib`/`seaborn` (Visualization), `scipy` (Statistics).
- **Architecture:**
  - `src/data_loader.py`: Centralized data fetching module.
  - `notebooks/`: Isolated analysis environments for each hierarchy level.
