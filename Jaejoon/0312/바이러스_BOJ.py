# 바이러스

# 컴퓨터의 수
N = int(input())

# 컴퓨터 쌍
computer = int(input())

graph = [[] for _ in range(N)]

# 무향 그래프
for i in range(computer):
     a, b = map(int,input().split())
     graph[a-1].append(b-1)
     graph[b-1].append(a-1)

visited = 0

# dfs
def connected(node):
    global visited

    # 방문 처리
    visited |= (1 << node)

    for next_node in graph[node]:
        # 아직 방문 안 했으면
        if visited & (1 << next_node) == 0:
            connected(next_node)

connected(0)

# visited에 1표시 되어있음 -> 1번 노드랑 연결되어 있다는 것
count = 0
for i in range(N):
    if visited & (1 << i):
        count += 1

# 1번 노드 자기자신은 제외
print(count-1)



