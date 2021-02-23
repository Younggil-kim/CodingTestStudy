from collections import deque
def solution(begin, target, words):
    answer = 0
    que = deque()
    #단어 하나 차이 나는경우로 스택을 계속 쌓아가면 될듯
    def check(n, start, end):
        cnt = 0
        for i in range(n):
            if start[i] == end[i]:
                cnt += 1
        return cnt
    que.append((begin, answer))
    while que:
        a, b = que.popleft()
        if a == target:
            answer = b
            break
        if b >= len(words):
            answer = 0
            break
        for word in words:
            if check(len(word), a, word) == len(word)-1:
                que.append((word,b+1))
    return answer