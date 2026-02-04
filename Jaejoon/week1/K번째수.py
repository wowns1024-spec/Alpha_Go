def solution(array, commands):
    answer = []
    lst = []
    new = []
    for idx in range(len(commands)):
        i, j, k = commands[idx]
        new = array[i-1:j]
        new.sort()
        answer.append(new[k-1])
    

    return answer