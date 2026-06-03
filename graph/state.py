from typing import TypedDict

import pandas as pd

class WorkflowState(TypedDict):
    data: pd.DataFrame
    execution_trace: list[str]
    cleaned_data: pd.DataFrame
    validation_report: dict
    quality_report: dict
    transformation_report: dict
    report: str