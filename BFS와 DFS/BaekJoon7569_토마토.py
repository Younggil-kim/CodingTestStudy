#7576과 비슷하나 2차원리스트가 아닌 3차원 리스트

#똑같이 진행하면 될듯

import sys
from collections import deque

M, N, K = map(int,sys.stdin.readline().split())

lst = list()
lstCopy = list()
for i in range(K):
    for j in range(N):
        lstCopy.append(list(map(int, sys.stdin.readline().split())))
    lst.append(list(lstCopy))
    lstCopy.clear()

#위 아래 앞 뒤 오른쪽 왼쪽
dx = [1, -1, 0, 0, 0, 0]#K에따라
dy = [0, 0, -1, 1, 0, 0]#N에따라
dz = [0, 0, 0, 0, 1, -1]#M에따라

#1인지점부터 bfs시작해야하니까 데큐 만들기
que = deque()

#익은 토마토가 있는 부분 큐에 다 좌표 집어넣기
for i in range(K):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 1:
                que.append((i,j,k))

def bfs():
    if len(que) == 0:
        return False
    else:
        while que:
            x, y, z = que.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx < 0 or nx >= K or ny < 0 or ny >= N or nz < 0 or nz >= M:
                    continue
                if lst[nx][ny][nz] == -1:#없는경우
                    continue
                if lst[nx][ny][nz] == 0:
                    lst[nx][ny][nz] = lst[x][y][z] + 1
                    que.append((nx,ny,nz))
        return True

bfs()
plg = False
maximum = 0
for i in range(K):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 0:
                plg = True
                break
            maximum = max(maximum, lst[i][j][k])
        if plg is True:
            break
    if plg is True:
        break
if plg is True:
    print(-1)
else:
    print(maximum-1)

