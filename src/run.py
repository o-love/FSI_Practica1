# Search methods

import search

def print_result(result_node: search.Node, type = "unknown"):
    print("----------------------------------------------------")
    print("Search Type:", type)
    print(result_node.path())
    print("Cost:", result_node.path_cost)
    print("----------------------------------------------------")

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print_result(search.breadth_first_graph_search(ab), "Breadth first")
print_result(search.depth_first_graph_search(ab), "Depth first")
print_result(search.best_first_graph_search(ab), "Best first")
print_result(search.heuristic_graph_search(ab), "Heuristic search")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
