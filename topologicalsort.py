from collections import deque
def dfs(graph, source, stack, visited):
    visited.add(source)
    for neighbour in graph[source]:
        if neighbour not in visited:
            dfs(graph, neighbour, stack, visited)
    stack.appendleft(source)

def topological_sort_of(graph):
    stack = deque()
    visited = set()
    for vertex in graph.keys():
        if vertex not in visited:
            dfs(graph, vertex, stack, visited)
    return stack

#if __name__=="__main__":
graph = {0:[1,2], 1:[2,5], 2:[3], 3:[], 4:[], 5:[3,4], 6:[1,5]}
topological_sort = topological_sort_of(graph)
print(topological_sort)