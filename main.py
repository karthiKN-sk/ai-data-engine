
from tools.csv_tools import load_csv
from graph.workflow import graph

df = load_csv("employees.csv")

result = graph.invoke(
    {
        "data": df,
    }
)

print("\nVALIDATION REPORT\n")
print(result["validation_report"])

print("\nQUALITY REPORT\n")
print(result["quality_report"])

print("\nTRANSFORMATION REPORT\n")
print(result["transformation_report"])

print("\nREPORT\n")
print(result["report"])

print("\nEXECUTION TRACE\n")
print(result["execution_trace"])