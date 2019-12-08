import numpy as np

##Function takes the graph from data and returns a tuple of its Vertices and the edges with thier weight values
def get_graph(textfile):
    edgelist = np.loadtxt(f'data/{textfile}', dtype = int)
    graph = ([],{})

    for vertex in edgelist:                                     ##iterates throught the list
        if vertex[0] not in graph[0]:                           ##adds the vertives as the first entry of the tuple
            graph[0].append(vertex[0])
    
        if vertex[1] not in graph[0]:                           ##adds the last vertex
            graph[0].append(vertex[1])

        graph[1][(vertex[0], vertex[1])] = vertex[2]            ##adds the edges and weights as the second value in the tuple
        
    return graph                                                ##returns tuple of vertices and edges with weights