def solution(brown, yellow):
    answer = []
    #1. 갈, 노랑 합쳐서 숫자부터 찾고 약수를 구해야할듯
    num = brown + yellow
    #2. 1부터 시작해서 num의 반까지 세로의 길이 먼저 찾고, 가로길이 찾기
    for i in range(2, num//2):
        if num % i == 0:
            row, col = num//i, i
            if 2*row + 2*(col-2) == brown:
                answer.append(row)
                answer.append(col)
                break
    return answer