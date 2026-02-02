# 껍데기(def)
def solution(array):
    # 1. 중복을 제거
    # 예: [1, 1, 2, 2] -> {1, 2}
    unique_numbers = list(set(array))
    
    # 2. 가장 많이 나온 횟수(max_count)
    max_count = 0
    for num in unique_numbers:
        # array.count(num)은 리스트 안에 num이 몇 개 있는지 세어줍니다.
        count = array.count(num)
        if count > max_count:
            max_count = count
            
    # 3. 최대 횟수만큼 나온 숫자들을 모두 모읍니다.
    # 예: 1도 2번, 2도 2번이면 -> [1, 2]가 모임
    best_numbers = []
    for num in unique_numbers:
        if array.count(num) == max_count:
            best_numbers.append(num)
            
    # 4. 정답 판단하기
    # 최빈값이 여러 개(리스트 길이가 1보다 큼)라면 -1
    if len(best_numbers) > 1:
        return -1
    # 하나라면 그 숫자가 정답
    else:
        return best_numbers[0]

