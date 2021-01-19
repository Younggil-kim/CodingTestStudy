#백준 1260

#주어진 입력에 따라서 DFS, BFS 탐색 결과 출력

#생각
#인접리스트 형태로 표현한 뒤 탐색한다.

import sys
from collections import deque

N, M, V = map(int,sys.stdin.readline().split())
lst = list()
for i in range(M):
    lst.append(list(map(int, sys.stdin.readline().split())))

grp = [[0]*(N+1) for _ in range(N+1)]
for i in lst:
    grp[i[0]][i[1]] = 1
    grp[i[1]][i[0]] = 1

# dfs 는 스택과 재귀를 이용

visit = [False] * (N + 1)
visit1 = [False] * (N+1)
result = []
def dfs(V,vst):

    vst.append(V)
    visit[V] = True
    a = vst.pop()
    result.append(a)
    for i in range(len(grp[a])):
        if grp[a][i] == 1 and visit[i] == False:
            dfs(i,vst)
    return result

def bfs(V):#bfs는 큐
    que = deque()
    que.append(V)
    result = [V]
    visit1[V] = True
    while que:
        a = que.popleft()

        for i in range(len(grp[a])):
            if grp[a][i] == 1 and visit1[i] == False:
                visit1[i] = True
                que.append(i)
                result.append(i)
    return result
print(*dfs(V,[]))
print(*bfs(V))
