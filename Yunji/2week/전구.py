N , M = map(int, input().split()) # N = 전구 개수, M = 명령어 개수
s = list(map(int,input().split())) # 전구 상태 받기
for _ in range(M):
    a,b,c = map(int, input().split()) # a, b, c에 각각에 부여된 데이터 받기
    # a = 명령어 번호 ,b= i or l ,c= x or r
    if a == 1 : # b번 전구를 c로 바꾸기
        s[b-1] = c
    elif a == 2 : # b 번 부터 c번까지 전구 상태 바꾸기 
        for i in range(b-1,c): # 인덱스 번호이므로 b-1, c-1까지 나타 내게함
            if s[i] == 0:
                s[i] = 1
            elif s[i] == 1:
                s[i] = 0
    elif a == 3 : # b 번 부터 c번까지 전구 상태 끄기
        for i in range (b-1,c):
            s[i] = 0
    elif a == 4 : # b 번 부터 c번까지 전구 상태 켜기
        for i in range (b-1,c):
            s[i] = 1
print (*s)