import sys
input = sys.stdin.readline
N = int(input())
km = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost = cost[:-1]
#첫번째 도시에서는 무조건 거리만큼 감
#이후에 거리를 더하면서 리터당 기름이 싼 지점까지 거리를 더해줌
# 그 결과를 res에 계속 더해주면됨

cur = cost[0]
res = 0
dis = km[0]
for i in range(1,N-1):
    if cur > cost[i]:#이후 나오는 기름값이 더 싸면
        res += dis*cur#이때까지 온거 계산
        dis = km[i]#거리 초기화
        cur = cost[i]
    else:#이후 나오는 기름값이 같거나 더 비싸면
        dis += km[i]
res += dis*cur
print(res)