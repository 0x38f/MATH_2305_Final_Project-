from functions.reading_writing_functions import get_graph
from algorithms.prims_algorithm import prims_mst_alg

dataChoice = input("Choose a graph from Data: ")
vertex = int(input("Choose a starting Vertex: "))

graph = get_graph(dataChoice)
minimumSpanningTree = prims_mst_alg(graph, vertex)

print('')
print(f'The minimum spanning tree for graph {dataChoice} is: {minimumSpanningTree[0]}')
print(f'The cost of the tree is {minimumSpanningTree[1]}')