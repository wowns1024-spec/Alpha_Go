def solution(array):
    # 개수 카운트용 리스트 생성 (인덱스 = 해당 원소)
    count = [0] * (max(array)+1)

    # 원소 개수 카운트
    for i in array:
        count[i] += 1
    
    # 리스트 내 최댓값의 인덱스 반환 = 원소 
    answer = count.index(max(count))

    # 같은 개수를 가지는 원소가 또 있는지 검사
    value = max(count)
    count.pop(count.index(max(count)))
    for i in count:
        if i == value:
            answer = -1

    return answer


# Test
print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
