import heapq
import sys

input = sys.stdin.readline

N = int(input())
lst = list()

for i in range(N):
    a = int(input())
    if a == 0:
        if len(lst) == 0:
            print(0)
        else:
            result = heapq.heappop(lst)
            print(result)
    else:
        heapq.heappush(lst,a)
