from collections import deque

# 안전 영역

# 지도 크기
N = int(input())

# 각 지역의 높이 정보
matrix = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 이동을 위한 델타 배열
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# BFS로 하나의 안전 영역을 탐색하는 함수
def flood(i, j, h):

    # BFS를 위한 큐 생성
    q = deque()

    # 시작 좌표를 큐에 넣기
    q.append((i, j))

    # 방문 처리
    visited[i][j] = 1

    # 큐가 빌 때까지 반복
    while q:

        # 현재 좌표 꺼내기
        i, j = q.popleft()

        # 상하좌우 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 범위 안인지 확인
            if 0 <= ni < N and 0 <= nj < N:

                # 아직 방문 안 했고
                # 현재 비 높이보다 높으면 (물에 잠기지 않은 지역)
                if visited[ni][nj] == 0 and matrix[ni][nj] > h:

                    # 방문 처리
                    visited[ni][nj] = 1

                    # 큐에 추가 (같은 안전 영역이므로 계속 탐색)
                    q.append((ni, nj))

# 지도에서 가장 높은 높이 찾기
max_height = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] > max_height:
            max_height = matrix[i][j]

# 안전 영역의 최대 개수
max_area = 0

# 비의 높이를 0부터 최대 높이까지 변화시키면서 확인
for h in range(max_height + 1):

    # 방문 여부 배열 초기화
    visited = [[0] * N for _ in range(N)]

    # 현재 비 높이에서의 안전 영역 개수
    area_cnt = 0

    # 모든 좌표 탐색
    for i in range(N):
        for j in range(N):

            # 물에 잠기지 않았고 아직 방문 안 했으면
            # 새로운 안전 영역 시작
            if matrix[i][j] > h and visited[i][j] == 0:

                # BFS로 연결된 지역 전부 방문 처리
                flood(i, j, h)

                # 안전 영역 하나 발견
                area_cnt += 1

    # 지금까지의 최대 안전 영역 갱신
    max_area = max(max_area, area_cnt)

# 결과 출력
print(max_area)