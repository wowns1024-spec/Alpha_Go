def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    visited = [[0] * M for _ in range(N)]
    start = (0, 0)
    visited[0][0] = 1
    q = []
    q.append(start)
    
    while q:
        i, j = q.pop(0)
        
        if i == N-1 and j == M-1:
            return visited[i][j]
        
        for di, dj in [[1, 0], [-1, 0], [0, 1],[0, -1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and maps[ni][nj] != 0 and visited[ni][nj] ==0:
                # 최단거리를 출력해야하니까 visited할때 +1 하는거 주의!
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    
    return -1
