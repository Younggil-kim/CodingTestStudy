N = int(input())

lst = list()

for i in range(N):
    lst.append(int(input()))

if N == 1:
    print(lst[-1])
elif N==2:
    print(sum(lst))
else:
    dp = [0]*(N+1)
    dp[0] = lst[0]#첫번째 계단을 밟은거
    dp[1] = lst[1] + lst[0]#첫번째계단과 두번째 계단을 밟은거
    dp[2] = max(lst[1] + lst[2] , lst[0] + lst[2])
    #세번째 계단은, 첫번째에서 바로 올라온건지, 두번째를 밟고 올라온건지

    for i in range(3,N):
        dp[i] = max(lst[i] + lst[i-1] + dp[i-3], lst[i] + dp[i-2])

    print(dp[N-1])