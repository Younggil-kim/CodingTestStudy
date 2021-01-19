#백준 2164번

#문제 해석
#N장의 카드가 놓여있을 때 제일 윗 카드를 버리고, 그 다음 카드를 제일 밑으로 보낸다
#마지막 카드는 무엇인가


#생각, 1~N까지 데큐에 다 집어 넣고, 동작을 반복한다.
#colletions의 deque를 쓰면 간단하다.
# 첫번째 동작은 제일 윗 카드 버리는거,1부터 순서대로 집어넣으면, popleft
# 두번째 동작은 popleft를 해서 제일 끝에 삽입.

N = int(input())
from collections import deque

que = deque()
for i in range(1,N+1):
    que.append(i)

while True:

    if len(que) == 1:
        print(que[0])
        break
    que.popleft()
    x = que.popleft()
    que.append(x)

