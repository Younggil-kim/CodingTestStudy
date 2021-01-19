
dp0 = [0] * 41
dp1 = [0] * 41

dp0[0] = 1
dp0[2] = 1

dp1[1] = 1
dp1[2] = 1

for i in range(3,41):
    dp0[i] = dp0[i-2] + dp0[i-1]
    dp1[i] = dp1[i-2] + dp1[i-1]

N = int(input())
for i in range(N):
    x = int(input())
    print(str(dp0[x]) + " " + str(dp1[x]))