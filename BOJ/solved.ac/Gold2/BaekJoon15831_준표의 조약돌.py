#백준 15831

N, B, W = map(int, input().split())
route = input()

tail = 0
curMax = 0

curWhite = 0
curBlack = 0
for head in range(N):
    #전진하면서 count 세어주기
    if route[head] == "W":
        curWhite += 1
    elif route[head] == "B":
        curBlack += 1
    #꼬리를 당겨오면서 W, B 계산해주기, 단, 조건에 따라서 B최대개수 아래, W 최대개수 위 생각하면서
    #W는 여기 반복문에서 체크 할 필요 없음, 아래에서 예외케이스로 잡아줘야 함

    while curBlack > B:
        if route[tail] == "W":
            curWhite -= 1
        elif route[tail] == "B":
            curBlack -= 1
        tail += 1
    if curWhite >= W:
        curMax = max( curMax, head - tail + 1)
print(curMax)
