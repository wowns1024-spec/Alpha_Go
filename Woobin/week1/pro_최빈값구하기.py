def solution(array):
    count = {}
    for i in array:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    max_value = 0
    max_number = 0
    
    for key in count:
        if count[key] > max_value:
            max_value = count[key]
            max_number = key
    
    if list(count.values()).count(max_value) > 1:
        return -1
    
    return max_number