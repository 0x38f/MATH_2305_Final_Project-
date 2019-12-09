from functions.reading_writing_functions import get_graph
from functions.graph_operations import init_tuple
from functions.graph_operations import incident_edges
from functions.graph_operations import edge_cost
from algorithms.prims_algorithm import prims_mst_alg

graph = get_graph("G2")                                 ##reads graph with filename and writes the edges and vertices with their weights

print(f'Graph vertices = {graph[0]}')                   ##Prints vertices
print('')
print(f'Graph edges and weights = {graph[1]}')          ##Prints edges and weights

vertex = init_tuple(0)

vertexEdges = incident_edges(graph, vertex)

print('')
print(f'{vertex[0]} is a member of edges {vertexEdges}')

cost = edge_cost(graph, (2, 3))

print('')
print(f'The cost of edge (2, 3) is: {cost}')

vertexEdgeCost = edge_cost(graph, vertexEdges[0])

print('')
print(f'The cost of edge {vertexEdges[0]} is: {vertexEdgeCost}')

minSpanningTree = prims_mst_alg(graph, 1)

print('')
print(minSpanningTree)

print('')
print(f'Minimum spanning tree: {minSpanningTree[0]}')
print(f'Minimum spanning tree cost: {minSpanningTree[1]}')