def solution(array):
    # 딕셔너리 활용해서 빈도수 세기 
    counts = {}
    for n in array:  
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    # 변수 설정
    max_count = 0
    result = 0

    # 딕셔너리를 돌며 최빈값 확인
    for num, count in counts.items():
        if count > max_count:
            
            max_count = count
            result = num
        elif count == max_count:
            # 만일 최빈 값이 여러개라면 -1 출력
            result = -1

    return result