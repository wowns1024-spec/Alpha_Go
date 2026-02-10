def solution(arr1, arr2):
    answer = []

    # 층수만큼 반복 (행)
    for i in range(len(arr1)):
        row = []  # 결과 바구니

        # 열
        for j in range(len(arr1[0])):
            sum = arr1[i][j] + arr2[i][j]
            row.append(sum)

        answer.append(row)

    return answer