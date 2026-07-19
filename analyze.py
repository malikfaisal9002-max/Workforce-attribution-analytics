"""
HR Attrition Analytics - Exploratory Data Analysis
Author: Mohammad Faisal
Dataset: IBM HR Analytics Employee Attrition (public, 1470 employees, 35 features)

This script computes the key attrition drivers used to power the Power BI-style
HTML dashboard included in this project.
"""

import pandas as pd
import json

df = pd.read_csv("../data/attrition.csv")

# Basic cleanup
df.columns = [c.strip() for c in df.columns]

summary = {}

# 1. Overall attrition rate
total = len(df)
left = (df["Attrition"] == "Yes").sum()
summary["overall"] = {
    "total_employees": int(total),
    "attrition_count": int(left),
    "attrition_rate_pct": round(left / total * 100, 1),
}

# 2. Attrition by department
dept = (
    df.groupby("Department")["Attrition"]
    .apply(lambda s: round((s == "Yes").mean() * 100, 1))
    .to_dict()
)
dept_counts = df["Department"].value_counts().to_dict()
summary["by_department"] = [
    {"department": k, "attrition_rate_pct": v, "headcount": int(dept_counts[k])}
    for k, v in dept.items()
]

# 3. Attrition by OverTime
ot = (
    df.groupby("OverTime")["Attrition"]
    .apply(lambda s: round((s == "Yes").mean() * 100, 1))
    .to_dict()
)
summary["by_overtime"] = [{"overtime": k, "attrition_rate_pct": v} for k, v in ot.items()]

# 4. Attrition by Job Role (top drivers)
role = (
    df.groupby("JobRole")["Attrition"]
    .apply(lambda s: round((s == "Yes").mean() * 100, 1))
    .sort_values(ascending=False)
    .to_dict()
)
role_counts = df["JobRole"].value_counts().to_dict()
summary["by_job_role"] = [
    {"job_role": k, "attrition_rate_pct": v, "headcount": int(role_counts[k])}
    for k, v in role.items()
]

# 5. Attrition by Job Satisfaction level (1=Low..4=Very High)
sat = (
    df.groupby("JobSatisfaction")["Attrition"]
    .apply(lambda s: round((s == "Yes").mean() * 100, 1))
    .to_dict()
)
summary["by_job_satisfaction"] = [
    {"level": int(k), "attrition_rate_pct": v} for k, v in sorted(sat.items())
]

# 6. Attrition by Years at Company (bucketed)
bins = [0, 2, 5, 10, 20, 100]
labels = ["0-2", "3-5", "6-10", "11-20", "20+"]
df["tenure_bucket"] = pd.cut(df["YearsAtCompany"], bins=bins, labels=labels, right=True)
tenure = (
    df.groupby("tenure_bucket", observed=True)["Attrition"]
    .apply(lambda s: round((s == "Yes").mean() * 100, 1))
    .to_dict()
)
summary["by_tenure"] = [{"tenure_years": k, "attrition_rate_pct": v} for k, v in tenure.items()]

# 7. Average monthly income: stayed vs left
income = df.groupby("Attrition")["MonthlyIncome"].mean().round(0).to_dict()
summary["avg_income_by_attrition"] = {
    "stayed": int(income.get("No", 0)),
    "left": int(income.get("Yes", 0)),
}

# 8. Attrition by Work-Life Balance (1=Bad..4=Best)
wlb = (
    df.groupby("WorkLifeBalance")["Attrition"]
    .apply(lambda s: round((s == "Yes").mean() * 100, 1))
    .to_dict()
)
summary["by_worklife_balance"] = [
    {"level": int(k), "attrition_rate_pct": v} for k, v in sorted(wlb.items())
]

# 9. Distance from home vs attrition (bucketed)
dbins = [0, 5, 10, 20, 30]
dlabels = ["0-5", "6-10", "11-20", "21-30"]
df["distance_bucket"] = pd.cut(df["DistanceFromHome"], bins=dbins, labels=dlabels, right=True)
dist = (
    df.groupby("distance_bucket", observed=True)["Attrition"]
    .apply(lambda s: round((s == "Yes").mean() * 100, 1))
    .to_dict()
)
summary["by_distance"] = [{"distance_km": k, "attrition_rate_pct": v} for k, v in dist.items()]

with open("../dashboard/data.json", "w") as f:
    json.dump(summary, f, indent=2)

print(json.dumps(summary, indent=2))
