
N = [0]*1001

for i in range(2, 1001):
    num = 1
    while True:
        if num * i >= 1001:  # 1001보다 같거나 커지면 브레이크
            break
        if N[num*i] == 0:
            N[num * i] = num
        num = num + 1

num = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if N[i] == 1:
        cnt = cnt + 1
print(cnt)