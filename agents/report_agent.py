from models.llm_router import LLMRouter
from models.model_type import ModelType


def report_agent(state: dict):
    router = LLMRouter()

    validation = state["validation_report"]
    transform = state["transformation_report"]

    report = router.generate_report(
        model=ModelType.CLAUDE,
        validation_report=validation,
        quality_report=state["quality_report"],
        transformation_report=transform,
    )


    trace = state["execution_trace"]

    return {
        **state,
        "execution_trace": [
            *trace,
            "report_agent",
        ],
        "report": report,
    }