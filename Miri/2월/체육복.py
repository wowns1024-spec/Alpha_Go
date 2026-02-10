def solution(n, lost, reserve):
    # 1. 모든 학생이 체육복을 1개씩 가지고 있다고 가정
    # 인덱스 0번은 안 쓰니까 n+1개 만들어서 1번부터 n번까지
    students = [1] * (n + 1)

    # 2. 잃어버린 학생은 -1 (체육복 0개가 됨)
    for l in lost:
        students[l] -= 1

    # 3. 여벌 있는 학생은 +1 (체육복 2개가 됨)
    for r in reserve:
        students[r] += 1

    # 4. 이제 1번 학생부터 n번 학생까지 순서대로 확인하며 빌려줌
    for i in range(1, n + 1):
        # 내가 체육복이 0개라면?
        if students[i] == 0:
            # 내 앞번호(i-1)가 2개를 가졌는지 확인
            if i - 1 >= 1 and students[i - 1] == 2:
                students[i] = 1
                students[i - 1] = 1
            # 앞번호는 없는데 뒷번호(i+1)가 2개를 가졌는지 확인
            elif i + 1 <= n and students[i + 1] == 2:
                students[i] = 1
                students[i + 1] = 1

    # 5. 마지막에 체육복이 1개 이상인 학생만 셉니다.
    answer = 0
    for i in range(1, n + 1):
        if students[i] >= 1:
            answer += 1

    return answer