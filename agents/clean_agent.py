

def clean_agent(state: dict):
    df = state["data"].copy()

    # remove duplicates
    df = df.drop_duplicates()

    # replace empty strings
    df = df.fillna("UNKNOWN")

    return {
        **state,
        "cleaned_data": df,
    }