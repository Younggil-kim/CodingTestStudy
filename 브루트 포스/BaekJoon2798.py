#백준 2798

#문제 해석
#합이 M을 넘지 않는 3장의 카드를 주어진 수 중에서 찾아라 

#생각
#브루트 포스니까 하나씩 경우의 수 다 생각한다.

N, M = map(int, input().split())
sum = 0
lst = list(map(int,input().split()))
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if lst[i] + lst[j] + lst[k] > M:
                continue
            else:
                sum = max(sum,lst[i] + lst[j] + lst[k])

print(sum)