#백준 2580 스도쿠

#문제
#스도쿠 형태가 주어지면 빈칸을 채워라

#풀이
#백트래킹 문제는 유망성검사가 공존한다.
#백트래킹은 모든 경우의 수를 다 찾는 브루트포스에서
# 특정 조건이 성립되면 가지치기가 되는 형태이다.
# 이 문제에서 유망성의 경우
# 1~9까지 있는 리스트를 만들고
# 행 기준, 열 기준, 3*3 박스 기준 으로 돌면서
# 숫자를 지우고 남은 숫자를 유망한 숫자로 만든다.
#

lst = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if lst[i][j] == 0]


def promise(i,j):
    nine = [1,2,3,4,5,6,7,8,9]
    #가로 세로 검사
    for s in range(9):
        if lst[i][s] in nine:# 행 검사
            nine.remove(lst[i][s])
        if lst[s][j] in nine:# 열 검사
            nine.remove(lst[s][j])

    #3*3 박스 검사
    i //= 3# 012, 345, 678 # 0 , 1 , 2
    j //= 3
    for k in range(i*3, (i+1)*3):
        for l in range(j*3, (j+1)*3):
            if lst[k][l] in nine:
                nine.remove(lst[k][l])

    return nine


exit_code = False
def seudoku(num):
    global exit_code

    if exit_code:
        return

    if num == len(blank):
        for x in lst:
            print(*x)
        exit_code = True
        return

    else:
        (i,j) = blank[num]
        promising = promise(i,j)

        for z in promising:
            lst[i][j] = z
            seudoku(num+1)
            lst[i][j] = 0

seudoku(0)