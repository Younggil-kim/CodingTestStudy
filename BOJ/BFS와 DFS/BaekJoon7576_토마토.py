#백준 7576 토마토문제

# 익었으면 1 아니면 0 없는칸은 -1이다
# 익은 토마토가 상하좌우 전염이됨
# 전체 전염시키는데 며칠이 걸리는지
# 근데 전부 전염 못시키면 -1출력

#익은 토마토가 있는 지점을 먼저 데큐에 넣어놓은 다음 진행해야
# 같이 큐에 들어가서 뽑아내서 쓸 수 있음

import sys
from collections import deque

M, N = map(int,sys.stdin.readline().split())
lst = list()
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

cnt = 1
dx = [-1,1,0,0]
dy = [0,0,1,-1]

que = deque()
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            que.append((i,j))

def bfs():
    if len(que) == 0:
        return False
    else:
        while que:
            x, y = que.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if lst[nx][ny] == -1:#썩어있으면
                    continue
                if lst[nx][ny] == 0:
                    lst[nx][ny] = lst[x][y] + 1
                    que.append((nx,ny))
        return True
bfs()
plg = False
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            plg = True

if plg is True:
    print(-1)
else:
    print(max(map(max, lst))-1)
