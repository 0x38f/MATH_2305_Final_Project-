import numpy as np

def get_graph():
    edgelist = np.loadtxt(f'data/G1.txt', dtype = int)
    G = ([],[])

    for x in edgelist:
        print(x)
        if x[0] not in G[0]:
            G[0].append(x[0])
        
        if x[1] not in G[0]:
            G[1].append( ( x[0],x[1] ) )

    return G

graph = get_graph()

print(f'V(G) = {graph[0]}')
print('')
print(f'E(G) = {graph[1]}')
