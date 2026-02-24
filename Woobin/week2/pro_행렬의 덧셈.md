- 만약 2차원 행렬의 크기가 [[1, 2, 3], [4, 5]] 이런 식으로 주어진다면 이 코드 틀림
- 좋은 코드 아님..
``` python
def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer
```
