# 게리맨더링 # 부분집합 연산자와 BFS를 이용해서 풀기
from collections import deque

# 구역의 개수 N
N = int(input())

# 각 구역의 인구
people = list(map(int,input().split()))

graph = [[] for _ in range(N)]

# 그래프 정보 받기
for i in range(N):
    info = list(map(int,input().split()))
    for j in info[1:]:
        graph[i].append(j-1)

# 그래프가 연결되어있는지 알 수 있게 해주는 함수
def connected(mask):

    # mask가 0이면 조건이 성립하지 않는다. => 지역구가 하나도 없다는거니까
    if mask == 0:
        return False

    # 시작 정점 찾기
    start = -1
    for i in range(N):
        if mask & (1 << i):
            start  = i
            break

    q = deque([start])
    # 출발점 관리 변수 설정
    visited_mask = 0
    # 출발점 방문처리
    visited_mask |= (1 << start)

    # BFS 탐색
    while q:
        x = q.popleft()
        for nx in graph[x]:
            # mask에 포함되어있는지? 방문했는지?
            if (mask & (1<<nx)) and not (visited_mask & (1 << nx)):
                # 방문 처리
                visited_mask |= (1<<nx)
                # q에 넣기
                q.append(nx)

    return visited_mask == mask

# 연결되어 있다면 값들을 더해서 반환해주는 함수
def pop_sum(mask):
    s = 0
    for i in range(N):
        if mask & (1 << i):
            s += people[i]

    return s

ALL = (1<<N) - 1 # 각 자리 전부 1로 ex) N=6 이면 ALL = 111111
ans = 10 ** 18 # 엄청 큰 수

# 대칭 제거 : 0과 ALL은 제외, 절반만 보면 됨
for mask in range(1, 1<<(N-1)):
    other = ALL ^ mask

    # 두 개다 True 일경우 구역이 잘 나누어진것
    if connected(mask) and connected(other):
        diff = abs(pop_sum(mask) - pop_sum(other))
        if diff < ans:
            ans = diff

print(ans if ans != 10 ** 18 else -1)
