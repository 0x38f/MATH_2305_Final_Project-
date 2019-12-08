from functions.reading_writing_functions import get_graph
from functions.graph_operations import incident_edges

graph = get_graph("G1")                                 ##reads graph with filename and writes the edges and vertices with their weights

print(f'Graph vertices = {graph[0]}')                   ##Prints vertices
print('')
print(f'Graph edges and weights = {graph[1]}')          ##Prints edges and weights

vertex = 0

vertexEdges = incident_edges(graph, vertex)

print('')
print(f'{vertex} is a member of edges {vertexEdges}')


