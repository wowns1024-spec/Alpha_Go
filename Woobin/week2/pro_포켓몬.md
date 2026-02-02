```python
def solution(nums):
    N = len(nums)
    nums.sort()
    answer = 1 
    for i in range(N-1):
        if answer == N//2: # nums가 2일때는 무조건 answer=1
            break
        if nums[i] != nums[i+1]:
            answer += 1
    return answer
```
