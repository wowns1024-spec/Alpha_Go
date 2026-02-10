# N개의 정수
N = int(input())
A = set(map(int, input().split()))

# 확인할 개수
M = int(input())

# 확인할 숫자들
targets = list(map(int, input().split()))

# 하나씩 꺼내서 확인하기
for num in targets:
    # 일단 0으로 가정
    answer = 0

    if num in A:
        answer = 1

    print(answer)