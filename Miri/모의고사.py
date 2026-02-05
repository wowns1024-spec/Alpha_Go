def solution(answers):
    # 1. 수포자 1, 2, 3번의 찍기 패턴을 리스트로 미리 정리! # 이건 데이터임
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 2. 각자 몇 문제나 맞혔는지 저장할 점수표야. (0번: 1번수포자, 1번: 2번수포자...) # 처음에는 다 0점
    scores = [0, 0, 0]
    
    # 3. 정답지(answers)를 하나씩 보면서 수포자들 답이랑 비교해보자.
    for i in range(len(answers)):
        # [핵심] 수포자 패턴은 짧고 문제는 많으니까 '%(나머지 연산)'으로 뱅글뱅글 돌려!
        if answers[i] == p1[i % len(p1)]:
            scores[0] += 1
        if answers[i] == p2[i % len(p2)]:
            scores[1] += 1
        if answers[i] == p3[i % len(p3)]:
            scores[2] += 1
            
    # 4. 세 사람 중에 가장 높은 점수가 몇 점인지 찾아보자.
    max_score = max(scores)
    
    # 5. 가장 높은 점수를 받은 사람(들)을 결과 리스트에 담아줄 거야.
    answer = []
    for idx, s in enumerate(scores):
        if s == max_score:
            # 사람 번호는 1번부터니까 인덱스(0, 1, 2)에 1을 더해줘야 해!
            answer.append(idx + 1)
            
    # 번호가 낮은 사람부터 담기니까(0번 인덱스부터 검사하니까) 자동으로 오름차순 정렬 완료!
    return answer