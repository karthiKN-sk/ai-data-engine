import pandas as pd


def transform_agent(state: dict):
    df = state["cleaned_data"].copy()

    # Convert salary to numeric
    df["salary"] = pd.to_numeric(
        df["salary"],
        errors="coerce",
    )

    avg_salary = float(df["salary"].mean())

    department_counts = (
        df["department"]
        .value_counts()
        .to_dict()
    )

    salary_by_department = (
        df.groupby("department")["salary"]
        .mean()
        )

    salary_by_department = {
        dept: (
            None
            if pd.isna(value)
            else round(float(value), 2)
        )
        for dept, value in salary_by_department.items()
    }
    print("salary_by_department",salary_by_department)

    transformation_report = {
        "average_salary": round(avg_salary, 2),
        "department_counts": department_counts,
        "average_salary_by_department":
            salary_by_department,
    }

    trace = state["execution_trace"]

    return {
        **state,
        "execution_trace": [
            *trace,
            "transform_agent",
        ],
        "transformation_report":
            transformation_report,
    }