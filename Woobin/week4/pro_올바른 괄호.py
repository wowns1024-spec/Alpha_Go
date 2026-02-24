def solution(s):
    answer = True
    stack = []
    for data in s:
        # 열린 괄호를 만나면 스택에 넣음
        if data == '(':
            stack.append(data)
        # 닫힌 괄호를 만났을 때         
        else:
            # 스택이 비어있으면 올바르지 않음
            if not stack:
                answer = False
                break
            # 스택이 비어있지 않을 때 스택에서 열린괄호 하나 뺌
            else:
                stack.pop()
    # s 안의 데이터를 다 돌았는데도 스택에 괄호가 남아있으면
    # 괄호 짝이 안맞다는 뜻이니까 올바르지 않음 
    if stack:
        answer = False

    return answer
