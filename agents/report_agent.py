def report_agent(state: dict):

    validation = state["validation_report"]
    transform = state["transformation_report"]

    total_rows = validation["total_rows"]
    errors = validation["error_count"]

    quality_score = round(
        ((total_rows - errors) / total_rows) * 100,
        2,
    )

    report = f"""
DATA QUALITY REPORT

Total Records: {total_rows}

Errors Found: {errors}

Quality Score: {quality_score}%

Average Salary:
{transform['average_salary']}

Department Counts:
{transform['department_counts']}

Recommendations:
- Fix invalid ages
- Fix invalid emails
- Fill missing salaries
"""

    return {
        **state,
        "report": report,
    }