import operator
from typing import Annotated, Any
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    web_results: Annotated[list, operator.add]
    vector_results: Annotated[list, operator.add]
    aggregate: Annotated[list, operator.add]

def search_web(state: State):
    print(f'Searching the web...')
    return {"web_results": ["results"]}


def search_vector_db(state: State):
    print(f'Searching the vector database...')
    return {"vector_results": ["results"]}

def aggregate_results(state: State):
    print(f'Aggregating results...')
    return {"aggregate": state["web_results"] + state["vector_results"]}

########################################################
# Here we are using the same nodes for the linear graph
########################################################
linear_graph = StateGraph(State)
linear_graph.add_node(search_web)
linear_graph.add_node(search_vector_db)
linear_graph.add_node(aggregate_results)
linear_graph.add_edge(START, "search_web")
linear_graph.add_edge("search_web", "search_vector_db")
linear_graph.add_edge("search_vector_db", "aggregate_results")
linear_graph.add_edge("aggregate_results", END)
linear_graph = linear_graph.compile()

# Generate PNG data
linear_graph.get_graph().draw_mermaid_png(output_file_path="linear_graph.png")


linear_graph.invoke({"aggregate": []})

########################################################
# Here we are using the same nodes for the parallel graph
########################################################
parallel_graph = StateGraph(State)
parallel_graph.add_node(search_web)
parallel_graph.add_node(search_vector_db)
parallel_graph.add_node(aggregate_results)
parallel_graph.add_edge(START, "search_web")
parallel_graph.add_edge(START, "search_vector_db")
parallel_graph.add_edge("search_web", "aggregate_results")
parallel_graph.add_edge("search_vector_db", "aggregate_results")
parallel_graph.add_edge("aggregate_results", END)
parallel_graph = parallel_graph.compile()

parallel_graph.get_graph().draw_mermaid_png(output_file_path="parallel_graph.png")

parallel_graph.invoke({"aggregate": []})