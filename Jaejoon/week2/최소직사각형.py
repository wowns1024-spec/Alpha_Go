# 최소직사각형

def solution(sizes):

    w_max = 0
    h_max = 0

    for w, h in sizes:
        # 긴 변을 w에 오게 정렬
        if w < h:
            w,h = h, w

        # 전체 최대값 갱신
        w_max = max(w_max, w)
        h_max = max(h_max, h)

    return w_max * h_max