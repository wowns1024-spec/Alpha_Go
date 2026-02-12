def solution(nums):
    #포켓몬 뽑을 수 있는 수
    ppop = len(nums) // 2

    #세트 사용
    good = set(nums)
    
    answer = 0
    
    if len(good) <= ppop:
        answer = len(good)
    
    if len(good) > ppop:
        answer = ppop

    
    return answer