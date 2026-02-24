``` python
def solution(arr):
    N = len(arr)
    
    answer = []
    for i in range(N):
        # answer이 비어있지 않아야 함.
        # answer에 가장 마지막에 넣은 값과 arr[i]값이 같으면(숫자가 연속으로 나올 때) append 안 함
        if answer and arr[i] == answer[-1]:
            continue
        
        # 그 외에는 다 append
        else:
            answer.append(arr[i])
        
    return answer
```
