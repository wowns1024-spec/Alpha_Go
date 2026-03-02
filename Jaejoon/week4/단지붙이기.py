# 단지붙이기

# 배열의 길이
N = int(input())

# 2차원 배열
matrix = [list(map(int,input())) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

sizes = []

# 재귀함수 안쓰고 풀어보기
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            # 방문처리
            matrix[i][j] = 0

            # 좌표 스택에 집어넣기
            stack = [(i,j)]

            # 카운트 변수 만들기
            count = 0

            # 탐색 시작
            while stack:
                si, sj = stack.pop()
                count += 1

                for k in range(4):
                    ni = si + di[k]
                    nj = sj + dj[k]

                    # 인덱스 범위 검사 and matrix 값이 1인지 검사
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 1:
                        # 방문처리
                        matrix[ni][nj] = 0
                        stack.append((ni,nj))

            sizes.append(count)

print(len(sizes))
sizes.sort()
for i in range(len(sizes)):
    print(sizes[i])