def solution(array, commands):
    answer = []
    for i in commands:
        sliced = sorted(array[i[0]-1:i[1]])
        answer.append(sliced[i[2]-1])
    return answer

# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# for 인덱싱에서 자꾸 에러가 나서 gpt 도움을 받았습니다..(참고 전 파일입니다)
#    for i in commands:
#       sliced = sorted(array[i[0]:i[1]])
#       answer.append(sliced[i[2]])