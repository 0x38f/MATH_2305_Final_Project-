from functions.reading_writing_functions import get_graph
from functions.graph_operations import init_tuple
from functions.graph_operations import incident_edges
from functions.graph_operations import edge_cost

##returns tree with shortest non-looping of a graph using the starting vertex and an empty tree
def prims_mst_alg(graph,x):

    vertex = init_tuple(x)                                          ##creates tuple of starting vertex and a blank tree
    mstSum = 0                                                      ##initializes minimum spanning tree sum

    while sorted(vertex[0])!=sorted(graph[0]):                      ##continues until all vertices are a member of the tree
        
        edges = (incident_edges(graph,vertex))                      ##sets edges to compare
        minimumCost = edge_cost(graph, edges[0])                    ##sets minimum cost to the cost of the first incident edge
        minimumCostEdge = edges[0]                                  ##sets edge with initial minimum cost (first incident edge)

        for edge in edges:                                          ##iterates through all incident edges
            if edge_cost(graph,edge) <=  minimumCost:               ##checks if the initial minimum cost is the actual minimum cost
                minimumCost = edge_cost(graph,edge)                 ##replaces initial minimum cost with true minimum cost
                minimumCostEdge = edge                              ##replaces edge with initial minimum cost with the true edge of minimum cost

        vertex[1].append(minimumCostEdge)                           ##adds edge to vertex tree

        for edgePoint in minimumCostEdge:                           ##itereates through current edge
            if edgePoint not in vertex[0]:                          ##checks to see if the next vertex is currently in the vertex list
                vertex[0].append(edgePoint)                         ##adds vertex to the vertex list

    for mstEdge in vertex[1]:                                       ##iterates through MST edges
            mstSum += edge_cost(graph , mstEdge)                    ##sums the cost of each edge

    return vertex[1], mstSum                                        ##returns tuple containing minimum spanning tree and cost sum
