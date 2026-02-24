def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(n+1):
        graph[i].sort()
    # print(graph)
    
    q = []
    q.append(1)
    visited = [0] * (n+1)
    visited[1] = 1
    
    while q:
        v = q.pop(0)
        for data in graph[v]:
            if visited[data] == 0:
                visited[data] = visited[v] + 1
                q.append(data)
                
    return visited.count(max(visited))
