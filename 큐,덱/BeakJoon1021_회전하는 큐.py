#백준 1021

#문제 해석
# 3가지 연산을 할 수 있는 덱으로,
# 1. leftpop, 2. leftpop 후 append, 3. pop 후 insertleft
# 처음 N개의 수가 있고, 뽑아내려하는 원소 위치가 있을 때
# 주어진 순서대로 뽑아드는데, 2,3번 연산의 최소값을 출력하라

# 첫줄에 큐의 크기 N과 뽑아내려고 하는 수 M이 주어진다.
# 둘째는 뽑아내려고하는 수의 위치가 순서대로 주어짐

#생각
# 2,3 연산이 최소로 되려면 가운데보다 오른쪽으면 오른쪽으로 빼고
# 가운데보다 왼쪽이면 왼쪽으로 계속 빼야 해
# 먼저 i가 어디있나부터 찾아야 함

from collections import deque

N, M = map(int, input().split())
lst = list(map(int,input().split()))
deq = deque()
for i in range(1,N+1):
    deq.append(i)
cnt = 0
for i in lst:
    while True:
        if i == deq[0]:
            deq.popleft()
            break
        if deq.index(i) > int(len(deq)/2):
            x = deq.pop()
            cnt = cnt+1
            deq.appendleft(x)
        else:
            x = deq.popleft()
            cnt = cnt + 1
            deq.append(x)

print(cnt)