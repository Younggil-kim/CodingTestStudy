#bfs이용
#R이면 오른쪽으로 가고, 방향조절은 자기 마음대로
#주문서 사용하면 또 못쓰게 완전탐색으로
from collections import deque


grp = list()
R, C, K = map(int, input().split())
for i in range(R):
    grp.append(list(map(int,input().split())))
print(grp)

check = False
que = deque()
def dfs():
    que.append((0,0))
    while que:
        if
        if x < 0 or x >= R or y < 0 or y >= C:
            return False
        if grp[x][y] == 'U':#위쪽이면
            nx, ny = x -1, y


        dfs(x-1,y,kleft,kright)#정방향 위로
        dfs()#주문서를 써서 오른쪽 90도 돌리면 오른쪽
        return True
    else:
        return False