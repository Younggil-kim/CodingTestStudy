# 1~N까지 돌면서 큐에 1번부터 집어넣고, 테이블을 True로 시켜주면서 다 돌고
# 이미 테이블에 트루면 무시하고, 아닌경우 다시 카운트 + 1
# 이 쉬운문제를 왤캐 오래 끈거야;
from collections import deque


def solution(n, computers):
    que = deque()
    table = [False for _ in range(n)]
    grp = [[] for _ in range(n)]
    cnt = []

    for i in range(n):#연결되어있는 부분 다 넣기
        for j in range(n):
            if computers[i][j] == 1:
                grp[i].append(j)

    def bfs():
        while que:
            nx = que.popleft()
            table[nx] = True
            for i in range(len(grp[nx])):
                if table[grp[nx][i]] is True:
                    continue
                que.append(grp[nx][i])
        cnt.append(1)

    for i in range(n):
        if table[i] is True:
            continue
        for j in range(len(grp[i])):
            que.append(grp[i][j])#아니면 큐에다 넣어버려
            table[i] = True
        bfs()#이미 방문한 노드면 bfs가 작동을 하면 안됨
    return len(cnt)

a =solution(3, [[1,1,0],[1,1,0],[0,0,1]])
print(a)