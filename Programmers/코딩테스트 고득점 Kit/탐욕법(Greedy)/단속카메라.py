def solution(routes):
    answer = 0
    routes.sort(key=lambda x :(-x[1]))
    cnt = 1
    a, b = routes.pop(-1)
    if len(routes) == 1:
        answer += 1
    else:
        while routes:
            x, y = routes.pop(-1)
            if x <= b <= y: #첫 차 진출시점이 두번째 범위 안에 있으면
                continue
            else: #첫 자 진출 시점이 두번째 범위 밖에 있으면
                cnt += 1
                b = y
        answer = cnt
    return answer