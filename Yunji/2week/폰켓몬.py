def solution(nums):
    nums.sort()

    limit = len(nums) // 2  # 뽑을 수 있는 마리 수
    cnt = 1                 # 첫 종류는 무조건 1개로 시작(아니면 값 부족!!)

    for i in range(len(nums) - 1):
        if nums[i] != nums[i+1]:
            cnt += 1
            if cnt == limit:
                break

    return cnt

