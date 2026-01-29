def solution(arry, commands):
    result = []
    for i, j, k in commands:
        sliced = arry[i-1:j]  # i~j 자르기 # 파이썬은 0부터 시작이니까 i-1 #여기서부터 GPT 도움 받으뮤ㅠ
        sliced.sort()  #정렬
        result.append(sliced[k-1]) # k번째 수 (k번째 -> k-1)
        #수정했음
    return result
