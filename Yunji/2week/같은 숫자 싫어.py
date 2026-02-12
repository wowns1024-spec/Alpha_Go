def solution(arr):
    answer = []
    for i in arr:
        if not answer or i != answer[-1]: 
            # 만약에 answer이 비었거나 마지막 원소와 i가 다르면 추가
            answer.append(i)
        elif i == answer[-1]:
            # 같으면 뛰어넘기
            continue
    return answer