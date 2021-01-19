#1번부터 n번까지 왔을때 최대값이 크면 그거로 가고
# 아니면 현재 최대값으로

n = int(input())
lst = list(map(int, input().split()))

grp = [0]*(n)

#왼쪽부터 더한값과 현재값 중 최대값

for i in range(n):
    grp[i] = max(grp[i-1] + lst[i], lst[i])

print(max(grp))