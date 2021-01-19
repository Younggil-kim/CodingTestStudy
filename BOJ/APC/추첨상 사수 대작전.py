

m, seed, x1, x2 = map(int, input().split())

# x1 + m*n = a* seed + c
# x2 + m*n = a* x1 + c
#n과 c의 연립방정식
n = 1

#m을 100아래까지 계속 넣어보자
for a in range(0,m):
    for c in range(0,m):
        v1, s1 = divmod(((a*seed +c) - x1) ,m)
        v2, s2 = divmod(((a*x1 + c) - x2),m)
        if v1 == v2 and s1 == s2:
            print(a, c)
            n = 0
            break
    if n == 0:
        break
