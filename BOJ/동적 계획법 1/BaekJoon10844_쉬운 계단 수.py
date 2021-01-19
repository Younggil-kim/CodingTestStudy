
N = int(input())
# 0으로 끝나면, 이전거는 1일 수밖에 없음
# 9로 끝나면 이전거는 8일수 밖에 없음

dp = [[0 for _ in range(10)] for i in range(N)]

dp[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]%1000000000
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]%1000000000
        else:#2로 끝나면 이전거가 1이거나 3
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]%1000000000

print(sum(dp[N-1])%1000000000)