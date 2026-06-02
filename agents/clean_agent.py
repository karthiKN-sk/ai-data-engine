

def clean_agent(state: dict):
    df = state["data"].copy()

    # remove duplicates
    df = df.drop_duplicates()

    # replace empty strings
    df = df.fillna("UNKNOWN")

    trace = state["execution_trace"]

    return {
        **state,
        "execution_trace": [
            *trace,
            "clean_agent",
        ],
        "cleaned_data": df,
    }