#백준 1697 숨바꼭질

#숫자가 두개 주어지고, 위치가 주어질때,
#어떻게 하면 제일 빨리 갈 수 있는지 구하라

#생각
#간단하게 리스트를 10만1개 만든 후
#인덱스와 값으로 bfs 돌리면 될듯

import sys
from collections import deque
N, K = map(int,sys.stdin.readline().split())

lst = [0 for _ in range(100001)]
lst[N] = 1

dx = [-1,1]

def bfs(x):
    que = deque()
    que.append(x)
    while que:
        x = que.popleft()
        for i in range(2):
            nx = x + dx[i]
            if nx < 0 or nx >= 100001:
                continue
            if lst[nx] == 0:
                que.append(nx)
                lst[nx] = lst[x] + 1
        nx2 = 2*x
        if nx2 < 0 or nx2 >= 100001:
            continue
        if lst[nx2] == 0:
            que.append(nx2)
            lst[nx2] = lst[x] + 1

bfs(N)

print(lst[K]-1)