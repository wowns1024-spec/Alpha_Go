def solution(array):
    answer = 0
    lst = []
    lst_2 = []
    
    #일단 array에 어떤 숫자들이 있는지 간추려 내고 싶다.
    for num in range(len(array)):
        if array[num] not in lst:
            lst.append(array[num]) #간추려서 빈 문자열 lst에 넣기.
            
        
    #간추린 숫자 카운트해서 몇개인지 파악
    for num in range(len(lst)):
        lst_2.append(array.count(lst[num]))
        
        
    #최빈값이 여러개면 lst_2.count(max(lst_2)) 했을때 1이 안나온다.
    if lst_2.count(max(lst_2)) != 1:
        return -1
    
    #lst에서 최빈값 인덱스와 lst_2에서 카운트한 최빈값의 인덱스가 맞아 떨어진다.
    else:
        answer = lst[lst_2.index(max(lst_2))]
        
    
    
    return answer


test_case = [1,1,2,3,3,3,4]

print(solution(test_case))