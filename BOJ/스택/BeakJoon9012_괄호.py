#백준 9012

# 문제 해석
# 괄호 쌍이 맞는지 아닌지 구하는문제

#생각
# 문자열 형태로 받은 뒤에 열린걸 스택에 집어넣고 닫힌게 나오면 하나씩 뺀다
# 이후에 스택의 길이가 0이면 YES 아니면 NO
import sys

N = int(sys.stdin.readline())

for i in range(N):
    stack = list()
    string = input()
    for j in string:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                stack.append(j)
                break
            else:
                stack.pop(-1)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")