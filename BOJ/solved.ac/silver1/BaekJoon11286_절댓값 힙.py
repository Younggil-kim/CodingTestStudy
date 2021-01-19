
import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
lst = PriorityQueue()
for i in range(N):
    a = int(input())
    if a == 0:
        if lst.empty():
            print(0)
        else:
            print(lst.get()[1])
    elif a > 0:#양수이면
        lst.put((a,a))
    elif a < 0:#음수이면
        lst.put((-a, a))