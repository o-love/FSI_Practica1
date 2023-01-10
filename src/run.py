# Search methods

import search


def print_result(result_node: search.Node, generated_nodes, visited_nodes, type = "unknown"):
    print("----------------------------------------------------")
    print("Search Type:", type)
    print(f"Generado: {generated_nodes}")
    print(f"Visitado: {visited_nodes}")
    print("Costo:", result_node.path_cost)
    print(f"Ruta: {result_node.path()}")
    print("----------------------------------------------------")


def run_all_searches_on_problem(start_char, end_char):
    print_result(*search.breadth_first_graph_search(search.GPSProblem(start_char, end_char, search.romania)), "Breadth first")
    print_result(*search.depth_first_graph_search(search.GPSProblem(start_char, end_char, search.romania)), "Depth first")
    print_result(*search.branch_and_bound_graph_search(search.GPSProblem(start_char, end_char, search.romania)), "Branch and Bound")
    print_result(*search.heuristic_graph_search(search.GPSProblem(start_char, end_char, search.romania)), "Heuristic search")


def run_romanian_search(start_char, end_char):
    print(f"\n\nStarting search from {start_char} to {end_char}")
    run_all_searches_on_problem(start_char, end_char)
    print(f"Done searching from {start_char} to {end_char}\n\n")

# NOTA: Las busquedas se tienen que realizar de uno en uno, sino se confunde con que nodo es el inicial y final. No he podido encontrar porque.
#run_romanian_search('A', 'B')
#run_romanian_search('O', 'E')
#run_romanian_search('G', 'Z')
#run_romanian_search('N', 'D')
#run_romanian_search('M', 'F')


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
