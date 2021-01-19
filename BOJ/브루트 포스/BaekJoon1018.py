#백준 1018

#2020-09-13 두번째 풀이

#흰색과 검은색이 공존하는 M*N크기의 보드에서
# 어떤 정사각형은 검은색, 나머지는 흰색으로 칠해져 있다.
# 이 보드를 잘라서 8*8 체스판을 만들려고 하는데
# 체스판은 체크무늬 형태로 칠해져있어야 한다.
# 보드에서 잘라냈을때, 바꿔서 칠해야 하는 색의 최소값을 구하라
# 체스판 색칠의 경우는 맨 왼쪽이 흰색인 경우, 검은색인 경우
# 두 가지 뿐이다.

# 생각
# 일단 전부 받아온다.
# N*M 판을 전체 경우의 수로 돌려야 한다.
# 그러기 위해서는 인덱스가 8을 넘지 않도록 조정을 해줘야 한다.
# 9*9에서 움직여서 조사할 수 있는 경우의 수는 2*2 4개이며,
# 10*10에서 움직여서 조사할 수 있는 경우의 수는 3*3 9개이고
# 11*11에서 움직여서 조사할 수 있는 경우의 수는 4*4 16개이다.
# 따라서, i는 N-7의 범위에서, j는 M-7의 범위에서 움직인다.
# 이후에 전체 경우의수를 다 돌면서
# W로 시작한 경우, B로 시작한 경우를 나누어서 판단한다.

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)

print(min(repair))
