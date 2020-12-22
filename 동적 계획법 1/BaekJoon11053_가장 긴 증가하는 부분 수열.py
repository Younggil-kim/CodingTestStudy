import bisect

N = int(input())
lst = list(map(int, input().split()))

result = list()

for i in lst:
    a = bisect.bisect_left(result, i)
    if a == len(result):
        result.append(i)
    else:
        #1 4 인데 2가 나오면 그 수랑 교체
        result[a] = i

print(len(result))