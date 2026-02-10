def solution(s):
    # 1. 바꿀 단어들을 사전처럼 준비
    # "단어"를 "글자 숫자"로 바꾸기
    words = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # 2. 사전에 있는 단어들을 하나씩 꺼내서 s 안에서 찾기
    for eng, num in words.items():
        # [핵심] s 안에 eng(단어)가 있으면 num(숫자)으로 싹 다 바꿔라!
        # 예: "one4seven" -> "14seven" -> "147"
        s = s.replace(eng, num)

    # 3. 마지막에 전체를 '진짜 숫자'로 바꿔서 반환
    return int(s)