
def solution(numbers, target):
    answer = []
    cnt = 0
    def dfs( cnt, n, target):
        if n >= len(numbers):
            if cnt == target:
                answer.append(1)
            return
        for i in range(n,len(numbers)):
            dfs( cnt + numbers[i], n + 1, target)
            dfs( cnt - numbers[i], n + 1, target)
            break
    dfs(cnt, 0,target)
    return len(answer)