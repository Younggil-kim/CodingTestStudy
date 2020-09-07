# 백준 10773

# 문제 해석
# 돈 관리하는 중에, 잘못된 수 부를때마다 0을 외쳐서 지운다.
# 모든 수를 받아 적고, 수의 합을 알고싶어 한다.

# 단순하게 받아와서 0이면 있던걸 빼주고, 아니면 스택에 추가


import sys

stack = list()
N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop(-1)
    else:
        stack.append(num)

print(sum(stack))