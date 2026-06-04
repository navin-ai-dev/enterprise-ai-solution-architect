from langgraph.graph import StateGraph

workflow = StateGraph(dict)

workflow.add_node("requirements")
workflow.add_node("userstories")
workflow.add_node("api")
workflow.add_node("database")
workflow.add_node("risk")
workflow.add_node("testcases")