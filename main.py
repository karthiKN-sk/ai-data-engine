from typing import TypedDict

import pandas as pd

from langgraph.graph import StateGraph
from langgraph.graph import END


from tools.csv_tools import load_csv

from agents.clean_agent import clean_agent
from agents.validate_agent import validate_agent
from agents.transform_agent import transform_agent
from agents.report_agent import report_agent


class WorkflowState(TypedDict):
    data: pd.DataFrame
    cleaned_data: pd.DataFrame
    validation_report: dict
    transformation_report: dict
    report: str


builder = StateGraph(WorkflowState)

builder.add_node("clean", clean_agent)
builder.add_node("validate", validate_agent)
builder.add_node("transform",transform_agent)
builder.add_node("report",report_agent)

builder.set_entry_point("clean")

builder.add_edge("clean", "validate")
builder.add_edge("validate","transform")
builder.add_edge("transform","report")
builder.add_edge("report", END)

graph = builder.compile()

df = load_csv("employees.csv")

result = graph.invoke(
    {
        "data": df,
    }
)

print("\nVALIDATION REPORT\n")
print(result["validation_report"])

print("\nTRANSFORMATION REPORT\n")
print(result["transformation_report"])

print("\nREPORT\n")
print(result["report"])