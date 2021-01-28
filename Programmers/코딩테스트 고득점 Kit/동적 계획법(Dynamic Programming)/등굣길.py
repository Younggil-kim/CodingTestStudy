def solution(m, n, puddles):
    grp = [[0 for _ in range(m)] for j in range(n)]
    while puddles:
        x, y = puddles.pop()
        grp[y - 1][x - 1] = -1
    # 물에 잠긴곳 체크
    for j in range(m):
        if grp[0][j] == -1:
            break
        grp[0][j] = 1
    for i in range(n):
        if grp[i][0] == -1:
            break
        grp[i][0] = 1
    # 가로세로 체크

    for i in range(1, n):
        for j in range(1, m):
            if grp[i][j] == -1:
                continue
            a = grp[i - 1][j]
            b = grp[i][j - 1]
            if a == -1 and b == -1:  # a,b 둘다 물이면 0
                grp[i][j] = 0
            elif a == -1 and b != -1:  # a만 물이면
                grp[i][j] = b
            elif a != -1 and b == -1:  # b만 물이면
                grp[i][j] = a
            else:
                k, grp[i][j] = divmod(a + b, 1000000007)
    answer = grp[-1][-1]
    return answer