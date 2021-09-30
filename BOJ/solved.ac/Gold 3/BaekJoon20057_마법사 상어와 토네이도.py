# 삼성 기출

import sys
input = sys.stdin.readline


leftList = [[0, -2, 0.05], [1, -1, 0.1], [-1, -1, 0.1], [1, 0, 0.07], [-1, 0, 0.07], [2, 0, 0.02], [-2, 0, 0.02], [1, 1, 0.01], [-1, 1, 0.01], [0, -1, 1]]
rightList = [[row, -col, rate] for row, col, rate in leftList]
downList = [[-col, row, rate] for row, col, rate in leftList]
upList = [[col, row, rate] for row, col, rate in leftList]

def sand(x,y, dir):
    global answer
    rest = 0
    dic = {0: leftList, 1: downList, 2: rightList, 3: upList}
    for row, col, rate in dic[dir]:
        if rate == 1:
            #나머지
            flyingSand = lst[x][y] - rest
        else:
            flyingSand = int(lst[x][y] * rate)
            rest += flyingSand
        if 0 <= x + row < n and 0 <= y + col < n:
            #내부에 존재하는경우
            lst[x+row][y+col] += flyingSand
        else:
            answer += flyingSand

def moveWind(x,y):
    dir = 0
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    while x != 0 or y != 0:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            x, y = nx, ny
            sand(nx, ny, dir)
            dir += 1
            if dir == 4:
                dir = 0
        else:
            dir -= 1
            if dir < 0:
                dir = 3

answer = 0
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
visited = [[0 for i in range(n)] for j in range(n)]

firstX, firstY = n//2, n//2
visited[firstX][firstY] = 1

moveWind(firstX,firstY)
print(answer)
