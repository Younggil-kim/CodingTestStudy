# 백준 10866

#문제 해석
# 덱을 만들어라
# 1. push_front X: 정수 X를 덱의 앞에 넣는다
# 2. push_back X : 정수 X를 덱의 뒤에 넣는다
# 3. pop_front 덱의 가장 앞 수 빼고 출력 없으면 -1
# 4. pop_back 덱의 가장 뒤 수 빼고 출력 없으면 -1
# 5. size 덱에 들어있는 정수 개수 반환
# 6. empty 비었으면 1 아니면 0
# 7. front 가장 앞 정수 출력 없으면 -1
# 8. back 가장 뒤 정수 출력 없는 경우 -1


import sys
N = int(input())
deq = list()
for i in range(N):
    command = sys.stdin.readline()
    command = command.split()
    if command[0] == "push_front":
        deq.insert(0,command[1])
    elif command[0] == "push_back":
        deq.append(command[1])
    elif command[0] == "pop_front":
        if len(deq) != 0:
            x = deq.pop(0)
            print(x)
        else:
            print("-1")
    elif command[0] == "pop_back":
        if len(deq) != 0:
            x = deq.pop(-1)
            print(x)
        else:
            print("-1")
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "empty":
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(deq) != 0:
            print(deq[0])
        else:
            print("-1")
    elif command[0] == "back":
        if len(deq) != 0:
            print(deq[-1])
        else:
            print("-1")