#백준 10828

#문제 해석
#정수를 저장하는 스택을 구현하고, 함수를 작성
# 1. push x 정수 X를 스택에 넣는 연산
# 2. pop 가장  위에 있는 정수를 빼고 출력, 없는 경우 -1 출력
# 3. szie 스택의 사이즈
# 4. empty 스택이 비어이쓰면 1 아니면 0
# 5. top 스택의 가장 위에 있는 정수 출력, 없는 경우 -1 출력


import sys
N = int(input())
stack = list()
for i in range(N):
    command = sys.stdin.readline()
    command = command.split()
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(stack) != 0:
            print(stack[-1])
            stack.pop(-1)
        else:
            print("-1")
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print("-1")