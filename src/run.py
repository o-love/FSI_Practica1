# Search methods

import search

def print_result(result_node: search.Node):
    print("new search")
    print(result_node.path())
    print("cost", result_node.path_cost)

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print_result(search.breadth_first_graph_search(ab))
print_result(search.depth_first_graph_search(ab))
print_result(search.best_first_graph_search(ab))


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
