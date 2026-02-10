def solution(nums):
    # 1. 내가 가져갈 수 있는 최대 마리 수 (N/2)
    # n/2가 소수가 나올 수 없으니 정수로 계산
    limit = len(nums) // 2

    # 2. 폰켓몬 종류가 총 몇 가지인지 확인하기
    # set() 중복 없애기
    unique_types = set(nums)
    type_count = len(unique_types)

    # 3. 가져갈 수 있는 한도(limit)와 종류 수(type_count)를 비교
    # 종류가 한도보다 많아도, 한도만큼만 가져갈 수 있어요.
    if type_count > limit:
        return limit
    # 종류가 한도보다 적으면, 그 종류를 다 가져가는 게 최선입니다.
    else:
        return type_count