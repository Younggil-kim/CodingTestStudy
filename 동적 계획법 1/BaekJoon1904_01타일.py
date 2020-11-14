# 11이 다 중복이되어버리네

N = int(input())
dp = [0]*(1000001)

dp[1] = 1#1짜리 하나
dp[2] = 2#00, 01

for i in range(3,N+1):
    dp[i] = (dp[i-2] + dp[i-1] )%15746
print(dp[N])