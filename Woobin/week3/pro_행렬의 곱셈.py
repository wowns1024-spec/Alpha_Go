def solution(arr1, arr2):
    # 행렬의 곱 특징: m x n * n x k = m x k
    k = len(arr1)
    n = len(arr1[0])
    m = len(arr2)
    answer = [[0]*m for _ in range(k)]
    
    for i in range(k):
        for t in range(n):
            for j in range(m):
                answer[i][j] += arr1[i][t] * arr2[t][j] 
    
    return answer
