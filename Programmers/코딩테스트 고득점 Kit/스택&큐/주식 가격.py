from collections import deque
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        cnt = 0
        #그러니까 제일 처음 나오는 작은 수 까지 insert를 계속 하면 됨
        start = prices[i]
        for j in range(i,len(prices)-1):
            if start <= prices[j]:
                cnt = cnt + 1
            else:
                answer.append(cnt)
                break
            if j == len(prices)-2:
                answer.append(cnt)
    answer.append(0)
    return answer