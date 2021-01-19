#백준 18258

#문제 해석
#큐를 구현하기

#명령은 6가지
#1. puxh x 정수 x를 큐에 넣는 연산
#2. pop 가장 앞 원소 빼고 출력, 비어있으면 -1 출력
#3.size 큐의 사이즈
#4. empty 비어있으면 1 아니면 0
#5. front 가장 앞에 있는 정수 출력 비어있으면 -1
#6. back 가장 뒤에 있는 정수 출력 비어있으면 -1

#스택에서 구현했던 것처럼 구현하면 시간초과가 난다.
# 명령의 수가 2,000,000까지이기 때문이다
# 이유는 pop에서 맨 앞을 빼고, 다시 당기는데 시간이 많이소요된다.
# 따라서 deque를 사용해서 popleft를 사용하는게 바람직하다.

#다른 방법은 좀 더 고민 해 봐야 할듯
import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([])
for i in range(N):
    command = sys.stdin.readline()
    command = command.split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
            queue.popleft()
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
