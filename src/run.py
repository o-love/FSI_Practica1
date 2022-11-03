# Search methods

import search


def print_result(result_node: search.Node, generated_nodes, visited_nodes, type = "unknown"):
    print("----------------------------------------------------")
    print("Search Type:", type)
    print(result_node.path())
    print("Cost:", result_node.path_cost)
    print(f"Generated Nodes: {generated_nodes}")
    print(f"Visited Nodes: {visited_nodes}")
    print("----------------------------------------------------")


def run_all_searches_on_problem(problem):
    print_result(*search.breadth_first_graph_search(problem), "Breadth first")
    print_result(*search.depth_first_graph_search(problem), "Depth first")
    print_result(*search.best_first_graph_search(problem), "Best first")
    print_result(*search.heuristic_graph_search(problem), "Heuristic search")


def run_romanian_search(start_char, end_char):
    print(f"\n\nStarting search from {start_char} to {end_char}")
    run_all_searches_on_problem(search.GPSProblem(start_char, end_char, search.romania))
    print(f"Done searching from {start_char} to {end_char}\n\n")


run_romanian_search('A', 'B')


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
