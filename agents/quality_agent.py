def quality_agent(state: dict):

    validation = state["validation_report"]

    total_rows = validation["total_rows"]

    error_count = validation["error_count"]

    quality_score = round(
        ((total_rows - error_count) / total_rows) * 100,
        2,
    )

    quality_report = {
        "quality_score": quality_score,
        "total_rows": total_rows,
        "error_count": error_count,
    }

    trace = state["execution_trace"]

    return {
        **state,
        "execution_trace": [
            *trace,
            "quality_agent",
        ],
        "quality_report": quality_report,
    }