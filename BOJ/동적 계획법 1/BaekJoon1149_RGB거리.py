N = int(input())
lst = list()
for i in range(N):
    lst.append(list(map(int, input().split())))

#0번째는, 1번 0번 // 2번 0번 미니멈
#1번째는, 0번 1번 // 2번 1번 미니멈
#2번째는, 0번 2번 // 1번 2번 미니멈

for i in range(1,N):
    for j in range(3):
        if j == 0:
            lst[i][j] = min(lst[i-1][1] + lst[i][j], lst[i-1][2] + lst[i][j])
        elif j == 1:
            lst[i][j] = min(lst[i-1][0] + lst[i][j], lst[i-1][2] + lst[i][j])
        else:
            lst[i][j] = min(lst[i-1][0] + lst[i][j], lst[i-1][1] + lst[i][j])

print(min(lst[N-1]))