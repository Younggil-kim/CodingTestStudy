N, K = map(int, input().split())
obj = [0]
weight = [0]
for i in range(N):
    a, b = map(int, input().split())
    obj.append(b)
    weight.append(a)

dp = [[0 for _ in range(K+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j < weight[i]:# j값은 지금 현재 최대 무게를 정하는건데 최대 K까지, 지금 현재 무게보다 넣을 무게가 커버리면 그냥 넘어가야됨
            dp[i][j] = dp[i-1][j]#그래서 그 경우에는 위쪽에서 가져와, 왜냐하면 아예 선택을 못하기 때문에, 그 윗 값이 최대값이 되기 때문
        else:
            dp[i][j] = max(obj[i] + dp[i-1][j-weight[i]], dp[i-1][j])#값을 선택하는경우 선택하지 않는경우

print(dp[N][K])
