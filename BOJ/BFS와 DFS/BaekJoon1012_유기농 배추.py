#백준 1012번
#배주 지렁이가 해충을 잡아먹으니까 최소 몇마리 필요한지
#연결되어 있는 곳에는 한마리만 있으면 됨

#간단하게 DFS로 훑으면서 진행하면 됨
# BFS로도 풀 수 있을 듯

#dfs 풀이
import sys

def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if lst[x][y] == 1:#배추가 있으면
        lst[x][y] = 2#방문 처리
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)#4방향 재귀
        return True
    else:
        return False

T = int(sys.stdin.readline())
sys.setrecursionlimit(3000)#이거 없으면 런타임

for i in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    lst = [[0]*M for _ in range(N)]
    cnt = 0
    for j in range(K):
        a, b = map(int, sys.stdin.readline().split())
        lst[b][a] = 1

    for l in range(N):
        for k in range(M):
            if dfs(l,k):
                cnt = cnt + 1
    print(cnt)


#bfs 풀이
import sys
from collections import deque

T = int(sys.stdin.readline())
sys.setrecursionlimit(3000)#이거 없으면 런타임

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []
def bfs(x,y):
    if lst[x][y] == 1:
        que = deque()
        que.append((x,y))
        lst[x][y] = 2
        while que:
            x , y = que.popleft()#젤 처음 배추인거 뽑고
            for i in range(4):#4방향으로 돌리고
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:#벽보다 크면 무시
                    continue
                if lst[nx][ny] == 0:#땅이면 무시
                    continue
                elif lst[nx][ny] == 1:#배추면
                    que.append((nx,ny))#큐에 추가
                    lst[nx][ny] = 2#방문
        return True

for i in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    lst = [[0]*M for _ in range(N)]
    cnt = 0
    for j in range(K):
        a, b = map(int, sys.stdin.readline().split())
        lst[b][a] = 1

    for l in range(N):
        for k in range(M):
            if bfs(l,k):
                cnt = cnt + 1
    print(cnt)
