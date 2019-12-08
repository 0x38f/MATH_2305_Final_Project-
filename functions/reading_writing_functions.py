import numpy as np

##Function takes the graph from data and returns a tuple of its Vertices and the edges with thier weight values
def get_graph(textfile):
    edgelist = np.loadtxt(f'data/{textfile}', dtype = int)
    G = ([],{})

    for x in edgelist:                                  ##Iterates throught the list
        if x[0] not in G[0]:                            ##adds the vertives as the first entry of the tuple
            G[0].append(x[0])
    
        if x[1] not in G[0]:                            ##adds the last vertice
            G[0].append(x[1])

        G[1][(x[0], x[1])] = x[2]                       #adds the edges and weights as the second value in the tuple
        
    return G