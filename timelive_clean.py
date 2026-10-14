"""
Timelive creates some very messy reports. This script cleans up the report and outputs a CSV with the total hours by employee and task.
"""

from collections import defaultdict

import pandas as pd

# excluded_months = ("/08/2026", "/09/2026")
excluded_months = ()

df = pd.read_csv(
    "LiveReport.csv",
    header=None,
    dtype=str,
    engine="python"
)

current_employee = None
totals = defaultdict(float)

for _, row in df.iterrows():

    col0 = "" if pd.isna(row[0]) else str(row[0]).strip()
    col4 = "" if pd.isna(row[4]) else str(row[4]).strip()
    col6 = "" if pd.isna(row[6]) else str(row[6]).strip()


    # Skip report junk/header rows
    if col0 in (
        "",
        "Selected Filters",
        "Employee Name",
    ):
        pass

    # Employee row:
    # name in col0 and everything else empty
    elif (
        col0
        and pd.isna(row[1])
        and pd.isna(row[2])
        and pd.isna(row[3])
        and pd.isna(row[4])
    ):
        current_employee = col0
        continue

    # Task row
    if current_employee and col4 and col6:
        # Skip excluded months
        if any(month in col4 for month in excluded_months):
            continue
        else:

            try:
                hours = float(col6)
            except ValueError:
                continue

            totals[(current_employee, col4)] += hours

output = pd.DataFrame(
    [
        [employee, task, hours]
        for (employee, task), hours in totals.items()
    ],
    columns=["Employee", "Task", "Hours"]
)

output = output.sort_values(
    ["Employee", "Task"]
)

print(output.to_string(index=False))

output.to_csv(
    "hours_by_employee_task.csv",
    index=False
)