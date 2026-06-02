import re


EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def validate_agent(state: dict):
    df = state["cleaned_data"]

    errors = []

    for index, row in df.iterrows():

        # AGE VALIDATION
        age = row["age"]

        if age == "UNKNOWN":
            errors.append({
                "row": index,
                "column": "age",
                "value": age,
                "error": "Missing age"
            })
        else:
            try:
                age_value = int(age)

                if age_value < 0:
                    errors.append({
                        "row": index,
                        "column": "age",
                        "value": age,
                        "error": "Negative age"
                    })

            except Exception:
                errors.append({
                    "row": index,
                    "column": "age",
                    "value": age,
                    "error": "Invalid integer"
                })

        # SALARY VALIDATION
        salary = row["salary"]

        if salary == "UNKNOWN":
            errors.append({
                "row": index,
                "column": "salary",
                "value": salary,
                "error": "Missing salary"
            })

        # EMAIL VALIDATION
        email = str(row["email"])

        if not re.match(EMAIL_REGEX, email):
            errors.append({
                "row": index,
                "column": "email",
                "value": email,
                "error": "Invalid email"
            })

    report = {
        "total_rows": len(df),
        "errors": errors,
        "error_count": len(errors)
    }

    return {
        **state,
        "validation_report": report
    }