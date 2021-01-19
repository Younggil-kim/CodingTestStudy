#문제 해석

# 신종 바이러스인 웜 바이러스는 네트워크 연결된거 전부 감염

#연결된 그래프가 있을때 감염된 컴퓨터를 구해라

#BFS와 DFS 둘 다 풀어보자

# DFS로 풀었을 경우
import sys


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

lst = list()
for i in range(K):
    lst.append(list(map(int, sys.stdin.readline().split())))

grp = [[0]*(N + 1) for _ in range(N+1)]
for i in lst:
    grp[i[0]][i[1]] = 1
    grp[i[1]][i[0]] = 1
visit = [False]*(N+1)
def dfs(start, vst):
    visit[start] = True
    vst.append(start)
    a = vst.pop()

    for i in range(len(grp[a])):
        if grp[a][i] == 1 and visit[i] is False:#미방문시
            dfs(i,vst)#방문
    return visit

print(dfs(1,[]).count(True)-1)


#BFS로 풀 경우
#너비 우선 탐색
import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

lst = list()
for i in range(K):
    lst.append(list(map(int, sys.stdin.readline().split())))

grp = [[0]*(N + 1) for _ in range(N+1)]
for i in lst:
    grp[i[0]][i[1]] = 1
    grp[i[1]][i[0]] = 1


def bfs(start):
    visit = [False] *(N+1)
    que = deque()
    que.append(start)#처음 방문

    visit[start] = True#처음은 트루
    while que:#BFS는 큐가 빌때까지 계속 전진
        a = que.popleft()#제일 먼저 들어간거 하나 빼
        for i in range(len(grp[a])):# 제일 먼저 들어간거 자손들 방문
            if grp[a][i] == 1 and visit[i] == False:#그게 미방문이면
                visit[i] = True#방문하고
                que.append(i)#큐에 집어넣어
    return visit

print(bfs(1).count(True)-1)
