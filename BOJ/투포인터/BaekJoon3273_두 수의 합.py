N = int(input())
lst = list(map(int, input().split()))
x = int(input())
lst.sort()

start = 0
end = len(lst)-1

cnt = 0
while start < end:
    if lst[start] + lst[end] < x:#타겟보다 더 작으면 수를 증가
        start = start + 1
    elif lst[start] + lst[end] > x:#타겟보다 더 크면 수를 감소
        end = end -1
    else:
        cnt = cnt + 1
        start = start + 1
        end = end -1
print(cnt)

