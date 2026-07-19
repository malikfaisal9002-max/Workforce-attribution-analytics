# Workforce attrition analytics

A business intelligence project identifying the drivers of employee attrition and quantifying where HR intervention would have the highest impact — built to mirror the kind of workforce reporting used at Eutech Chambers and Human Resource Development Society.

**[View the live dashboard](./dashboard/index.html)** ([screenshot below](#dashboard-preview))

## Business problem

Organizations lose significant time and cost every time an employee leaves — recruiting, onboarding, and lost productivity all add up. This project answers three questions an HR or people-analytics team would actually ask:

1. Which departments and job roles have the highest attrition, and how big are those groups?
2. What working conditions (overtime, distance from home, tenure, satisfaction) correlate most strongly with people leaving?
3. Where should retention budget go first?

## Key findings

- **Overtime is the strongest single driver.** Employees working overtime leave at **30.5%**, nearly 3x the rate of those who don't (**10.4%**).
- **Attrition is front-loaded.** Employees in their first 2 years leave at **28.9%**, dropping to under 13% after year 3 — the highest-risk window is onboarding through year two, not long-tenured staff.
- **Sales Representatives are the highest-risk role** at **39.8%** attrition, nearly 4x the company average.
- **Pay is not the whole story.** Average income for employees who left ($4,787/month) is lower than those who stayed ($6,833/month), but satisfaction and work-life balance move attrition even within similar pay bands.
- **Commute matters.** Attrition rises from 13.8% (0–5 km from home) to 22.1% (21–30 km), suggesting remote/hybrid flexibility could be a retention lever.

## Dashboard preview

The dashboard (`dashboard/index.html`) is a self-contained, Power BI-style HTML report — KPI tiles, department/role breakdowns, a tenure risk curve, and satisfaction vs. work-life balance comparison. Built with Chart.js so it's viewable directly in any browser with no server required.

## Repository structure

```
hr-attrition-project/
├── data/
│   └── attrition.csv              # IBM HR Analytics dataset (public, 1,470 employees)
├── analysis/
│   └── analyze.py                 # pandas EDA — computes every metric behind the dashboard
├── dashboard/
│   ├── index.html                 # Interactive HTML dashboard (Chart.js)
│   └── data.json                  # Aggregated metrics consumed by the dashboard
└── README.md
```

## Tools and methods

- **Python (pandas)** for data cleaning, grouping, and aggregation
- **Chart.js** for the interactive dashboard front-end
- Techniques used: group-by aggregation, bucketing/binning continuous variables (tenure, distance), rate calculations, comparative KPI analysis — the same analytical building blocks used in Power BI/DAX measures and Tableau calculated fields

## How to reproduce

```bash
cd analysis
pip install pandas
python analyze.py        # regenerates dashboard/data.json
```

Then open `dashboard/index.html` in any browser.

## Data source

[IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) — a public, fictional dataset released by IBM for analytics practice. 1,470 employee records, 35 attributes.

## Author

**Mohammad Faisal** — Business Intelligence Analyst, 19+ years in HR reporting, workforce analytics, and BI development (Power BI, Tableau, SQL, DAX).
[LinkedIn](https://www.linkedin.com/in/muhammed-faisal-214255121)
