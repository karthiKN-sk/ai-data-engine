def supervisor_agent(state: dict):

    print("\n[Supervisor] Starting workflow")

    return {
        **state,
        "execution_trace": ["supervisor"],
    }