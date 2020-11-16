#백준 2206 벽 부수고 이동하기

#벽을 최소 한번은 부술 수 있다는 소리
# 그러니까 벽의 위치를 좌표로 다 받아와서
# 하나씩 지워보면서 완전탐색을 해야함

from collections import deque

N, M = map(int,input().split())

lst = list()
for i in range(N):
    lst.append(list(map(int, input())))


wall = deque()
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            wall.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x, y):
    que = deque()
    lst[x][y] = 1
    que.append((x,y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if lst[nx][ny] == 1:
                continue
            if lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y] + 1
                que.append((nx,ny))
    return True
bfs(0,0)
result = []
result.append(lst[N-1][M-1])

wallCopy = wall.copy()
def newList():
    new = [[0 for i in range(M)] for j in range(N)]
    for i in range(len(wallCopy)):
        x, y = wallCopy[i]
        new[x][y] = 1
    return new

while wall:
    lst = newList()
    x, y = wall.popleft()
    lst[x][y] = 0
    bfs(0,0)
    result.append(lst[N - 1][M - 1])

result = list(set(result))
result.remove(0)
if len(result) == 0:
    print(-1)
else:
    print(min(result))