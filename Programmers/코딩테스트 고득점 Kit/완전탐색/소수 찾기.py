def chk(n):
    lst = [True]*(n+1)
    m = int((n+1)**0.5)
    for i in range(2,m+1):
        if lst[i] is True:
            for j in range(i+i,n+1,i):
                lst[j] = False
    return [i for i in range(2,n+1) if lst[i] is True]

def solution(numbers):
    answer = 0
    result = set()
    len_numbers = len(numbers)
    table = [False]*(len_numbers)
    def dfs(n,num,length):
        if n == length+1:
            return
        else:
            result.add(int(num))
            for i in range(len_numbers):
                if table[i] is True:
                    continue
                table[i] = True
                dfs(n+1, num + numbers[i],length)
                table[i] = False
    s = "0"
    dfs(0,s,len_numbers)
    cnt = 0
    chklist = chk(max(result))
    for i in result:
        if i in chklist:
            cnt = cnt + 1
    answer = cnt
    return answer