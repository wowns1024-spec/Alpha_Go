- 내가 푼 코드
```python
def solution(answers):
    N = len(answers)
    person1 = [1, 2, 3, 4, 5] 
    if N <= 5:
        person1 = person1[:N] 
    else:
        person1 = [1, 2, 3, 4, 5] * (N//5)
        if N % 5 >0:
            person1.extend(person1[:(N%5)])
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    if N <= 8:
        person2 = person2[:N]
    else:
        person2 = [2, 1, 2, 3, 2, 4, 2, 5] * (N // 8)
        if N % 8 >0:
            person2.extend(person2[:(N%8)])
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    if N <= 10:
        person3 = person3[:N]
    else:
        person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (N // 10)
        if N % 10 >0:
            person3.extend(person3[:(N%10)])
    count = [0, 0, 0]
    for i in range(N):
        if person1[i] == answers[i]:
            count[0] += 1
        if person2[i] == answers[i]:
            count[1] += 1
        if person3[i] == answers[i]:
            count[2] += 1
    
    max_score = max(count)
    answer = []
    for i in range(3):
        if count[i] == max_score:
            answer.append(i + 1)

    return answer
```
- gpt 코드
``` python
def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]
    for i, a in enumerate(answers):
        if a == p1[i % len(p1)]: cnt[0] += 1
        if a == p2[i % len(p2)]: cnt[1] += 1
        if a == p3[i % len(p3)]: cnt[2] += 1

    m = max(cnt)
    return [i + 1 for i, c in enumerate(cnt) if c == m]
```
