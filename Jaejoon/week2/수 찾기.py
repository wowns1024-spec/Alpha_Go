# 자연수 N
N = int(input())

# N 개의 정수
arr_n = set(map(int, input().split())) # 애초에 받아올때 set로 받아오기

# 자연수 M
M = int(input())

# M개의 수
arr_m = list(map(int, input().split()))

# arr_m 하나씩 꺼내서 arr_n에 있는지 확인하기
for i in arr_m:
    if i in arr_n:
        print(1)
    else:
        print(0)
















##################################################

# 수 찾기

# # 자연수 N
# N = int(input())
#
# # N 개의 정수
# arr_n = list(map(int, input().split()))
#
# # 자연수 M
# M = int(input())
#
# # M개의 수
# arr_m = list(map(int, input().split()))
#
# # M개의 수들이 arr_n에 존재하는지 알아보자
# for i in range(M): # arr_m 전용
#     for j in range(N): # arr_n 전용
#         if arr_m[i] == arr_n[j]:
#             print(1)
#             break # for j
#
#     else:
#         print(0)

# 이렇게 푸니까 시간초과 난다.
# 이중 for문은 시간복잡도가 n^2
# 문제 제한이
# N <= 100,000
# M <= 100,000
# 최악의 경우 100억 번 비교 해야되서 무조건 시간초과

##################################################

