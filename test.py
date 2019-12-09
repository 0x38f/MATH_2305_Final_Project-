from functions.reading_writing_functions import get_graph
from functions.graph_operations import incident_edges
from functions.graph_operations import edge_cost

graph = get_graph("G1")                                 ##reads graph with filename and writes the edges and vertices with their weights

print(f'Graph vertices = {graph[0]}')                   ##Prints vertices
print('')
print(f'Graph edges and weights = {graph[1]}')          ##Prints edges and weights

vertex = 0

vertexEdges = incident_edges(graph, vertex)

print('')
print(f'{vertex} is a member of edges {vertexEdges}')

cost = edge_cost(graph, (2, 3))

print('')
print(f'The cost of edge (2, 3) is: {cost}')

vertexEdgeCost = edge_cost(graph, vertexEdges[1])

print('')
print(f'The cost of edge {vertexEdges[1]} is: {vertexEdgeCost}')


