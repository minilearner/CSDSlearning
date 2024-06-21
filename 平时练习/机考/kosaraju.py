graph = [[1], [2, 4], [3, 5], [0, 6], [5], [4], [7], [5, 6]]

def dfs1(graph,node,visited,stack):

    visited[node]=True
    for next in graph[node]:
        if not visited[next]:
            dfs1(graph,next,visited,stack)
    stack.append(node)

def dfs2(graph,node,component,visited):

    visited[node]=True
    component.append(node)
    for next in graph[node]:
        if not visited[next]:
            dfs2(graph,next,component,visited)




def kosaraju(graph):
    n = len(graph)
    visited = [False for i in range(n)]
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs1(graph,i,visited,stack)

    visited = [False for i in range(n)]
    sscs = []
    transposed_graph=[[]for i in range(n)]
    for i in range(n):
        for v in graph[i]:
            transposed_graph[v].append(i)
    while stack:
        t = stack.pop()

        if not visited[t]:
            ssc =[]
            dfs2(transposed_graph,t,ssc,visited)
            sscs.append(ssc)
            print(ssc)
    return sscs

temp = kosaraju(graph)

