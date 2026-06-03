
from langgraph.graph import StateGraph
from langgraph.graph import END


from agents.supervisor_agent import supervisor_agent
from agents.clean_agent import clean_agent
from agents.validate_agent import validate_agent
from agents.quality_agent import quality_agent
from agents.transform_agent import transform_agent
from agents.report_agent import report_agent
from graph.state import WorkflowState

builder = StateGraph(WorkflowState)

builder.add_node("supervisor",supervisor_agent)
builder.add_node("clean", clean_agent)
builder.add_node("validate", validate_agent)
builder.add_node("quality",quality_agent)
builder.add_node("transform",transform_agent)
builder.add_node("report",report_agent)

builder.set_entry_point("supervisor")

builder.add_edge("supervisor","clean")
builder.add_edge("clean", "validate")
builder.add_edge("validate", "quality")
builder.add_edge("quality","transform")
builder.add_edge("transform","report")
builder.add_edge("report", END)

graph = builder.compile()