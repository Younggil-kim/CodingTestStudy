dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9

for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

case = int(input())
for i in range(case):
    x = int(input())
    print(dp[x])
