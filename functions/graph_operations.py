##takes an integer and creates a tuple
def init_tuple(x):
    return ([x],[])

##finds all edges a vertex is a member of
def incident_edges(graph, vertexTuple):

    edges = []                                                                                  ##initializes list for edges

    for edge in graph[1]:                                                                       ##iterates through all graph edges
        for vertex in vertexTuple[0]:                                                           ##iterates until vertex
            if vertex in edge:                                                                  ##checks if vertex is a member of the edge
                if edge not in vertexTuple[1]:                                                  ##checks if edge is in vertcies tuple
                    if ((edge[0] not in vertexTuple[0]) or (edge[1] not in vertexTuple[0])):    ##checks if graph edge has been added
                        
                        edges.append(edge)                                                      ##adds graph edge to edges list

    return edges                                                                                ##returns list of edges that vertex is a member of

##takes a graph and an edge in the graph, returns the cost of the edge
def edge_cost(graph,edge):
    return graph[1][edge]