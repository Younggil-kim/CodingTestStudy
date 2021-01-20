def solution(array, commands):
    answer = []
    for cmd in commands:
        i, j, k = cmd
        check = array[i-1:j]
        check.sort()
        answer.append(check[k-1])
    return answer