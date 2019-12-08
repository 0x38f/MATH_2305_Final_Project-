from functions.reading_writing_functions import get_graph

graph = get_graph("G1.txt")                             ##reads graph with filename and writes the edges and vertices with their weights

print(f'Graph vertices = {graph[0]}')                   ##Prints vertices
print('')
print(f'Graph edges and weights = {graph[1]}')          ##Prints edges and weights