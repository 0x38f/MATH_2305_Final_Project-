from functions.reading_writing_functions import get_graph
from functions.graph_operations import init_tuple
from functions.graph_operations import incident_edges
from functions.graph_operations import edge_cost
from algorithms.prims_algorithm import prims_alg

graph = get_graph("G1")                                 ##reads graph with filename and writes the edges and vertices with their weights

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

vertexEdgeCost = edge_cost(graph, vertexEdges[1])

print('')
print(f'The cost of edge {vertexEdges[1]} is: {vertexEdgeCost}')

minSpanningTree = prims_alg(graph, 0)

print('')
print(f'{minSpanningTree}')

testTriplette = ([0],[], 0)
testTriplette[1].append(1)


print('')
print(type(testTriplette[2]))