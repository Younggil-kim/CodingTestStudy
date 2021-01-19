#백준 1874

#문제 해석
#자연수 N까지 오름차순으로 스택에 넣으면서
#입력되는 수열을 푸쉬와 pop으로 만들어라

#생각
# 먼저 스택을 만들고
# 스택에다 집어넣으면서 만들어야 하는 수열의 첫 부분이
# 나올때까지 계속 푸쉬.
# 이후에 푸쉬한게 같으면 팝
# 그 다음 수열도 마찬가지로 만들기

#못만드는 경우는 어떤 경우일까?
#seq에 남아있는 경우는 못만드는 경우
#한번에 모아서 출력해주면 해결

# 수열을 전부다 받아오고하면 복잡해
# 그러니까 수열을 받자마자 바로 푸쉬를 해주는게 좋아보여
import sys
N = int(sys.stdin.readline())
stack = list()
result = list()
cnt = 1
impossible = False
for i in range(1,N+1):
    seq = int(input())
    while cnt <= seq: #cnt를 증가시켜 언제까지?
        stack.append(cnt)
        result.append("+")
        cnt = cnt + 1
    if stack[-1] == seq:
        stack.pop()
        result.append("-")
    else:
        impossible = True
if impossible is True:
    print("NO")
else:
    for i in result:
        print(i)