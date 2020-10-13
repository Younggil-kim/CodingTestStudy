#백준 2667번 단지 번호 붙이기

# 단지 수를 출력하고, 각 단지에 속하는 세대 수를 출력하라

# dfs로
# import sys
# N = int(sys.stdin.readline())
#
# lst = list()
# for i in range(N):
#     lst.append(list(map(int,input())))
#
#
# cnt = 0
# num = []
# result = []
# def dfs(x,y):
#     if x < 0 or x >=N or y < 0 or y >= N:
#         return False
#     if lst[x][y] == 1:#아파트가 있으면
#         lst[x][y] = 2#방문하고
#         num.append([x,y])#있는 위치 기록
#         dfs(x + 1,y)
#         dfs(x - 1, y)
#         dfs(x, y + 1)
#         dfs(x, y - 1)
#         return True
#     else:
#         return False
#
#
#
# for i in range(N):
#     for j in range(N):
#         if dfs(i,j):# 한 덩어리 나오면
#             cnt = cnt + 1# 단지 수 하나 올리고
#             result.append(len(num))# 세대수 하나 올리고
#         num.clear()#리스트 초기화
# result.sort()
# print(cnt)
# for i in result:
#     print(i)
#

#bfs로
import sys
from collections import deque
N = int(sys.stdin.readline())

lst = list()
for i in range(N):
    lst.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


cnt = 0
num = []
result = []
def bfs(x,y):
    if lst[x][y] == 1:
        global cnt
        que = deque()
        que.append((x,y))
        lst[x][y] = 2
        result.append([x, y])
        while que:
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >=N:
                    continue
                if lst[nx][ny] == 0:#길이면 그냥
                    continue
                if lst[nx][ny] == 1:# 아파트면?
                    lst[nx][ny] = 2
                    que.append((nx,ny))
                    result.append([nx,ny])
        return True





for i in range(N):
    for j in range(N):
        if bfs(i,j):
            cnt = cnt + 1
            num.append(len(result))
        result.clear()

print(cnt)
num.sort()
for i in num:
    print(i)
