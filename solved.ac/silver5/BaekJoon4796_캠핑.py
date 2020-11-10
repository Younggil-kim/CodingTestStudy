#문제 해석
#캠핑장은 연속하는 P일 중 L일 동안 사용가능하고, V일짜리 휴가 시작했을때
#최대 며칠동안 캠핑장을 사용할 수 있는가?

i = 0
while True:
    i = i + 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    day = ((V // P) * L) + min( V%P, L)
    print("Case " + str(i) + ": " + str(day))