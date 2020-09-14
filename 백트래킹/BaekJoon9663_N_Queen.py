#백준 9663

#문제 해석
#크기가 N*N인 체스판에 퀸 N개를 서로 공격할 수 없게 놓기
#N이 주어졌을때 퀸을 놓는 방법의 수를 구하라


#세로 줄, 대각선 줄, 역대각선 줄 배열을 만든다.
# 이 세 개의 배열로 놓아도 되는지 안되는지 정당성을 판단한다

N = int(input())
result = 0

row = list(False for i in range(N))
diagonal = list(False for j in range(2*N-1))
indiagonal = list(False for k in range(2*N-1))

def Nqueen(i):
    global result
    if i == N:
        result += 1
        return
    else:
        for j in range(N):
            if not (row[j] or diagonal[i+j] or indiagonal[i-j+N-1]):# 셋 전부 False인 경우
                row[j] = diagonal[i+j] = indiagonal[i-j+N-1] = True # 대각선, 역대각선, 세로 전부 True로 변경
                Nqueen(i + 1)# 다음 행에 대해 진행
                row[j] = diagonal[i + j] = indiagonal[i - j + N - 1] = False #초기화

Nqueen(0)
print(result)
