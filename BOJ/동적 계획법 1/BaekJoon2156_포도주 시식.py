N = int(input())

lst = list()

for i in range(N):
    lst.append(int(input()))

dp = [0] * (N)

if N <= 2:
    print(sum(lst))
else:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[2], lst[1] + lst[2], lst[0] +lst[1])
    for i in range(3,N):
        dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2]  + lst[i])
        dp[i] = max(dp[i-1],dp[i])
        #계단오르기와 비슷하지만
        # 두번 연속 안먹어도 될 경우가 있기때문에
        # 두번째 점화식이 필요
    print(dp[N-1])
