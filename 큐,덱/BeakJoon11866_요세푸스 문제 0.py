#백준 11866 요세푸스 문제

#문제 해석
# 1부터 N까지의 사람이 둘러앉아 있을 때
# K번째 사람을 죽이고, 계속해서 k번째 사람을 죽이면
# 그게 요세푸스 순열이다.
# 순열을 구하라

# 생각
# 데큐를 만들어, 그래서, 레프트팝을하고 푸쉬를 하는데 3이 되면 팝만하고
# 리스트에 추가 이게 순열이 될 것

from collections import deque

N, K = map(int, input().split())
que = deque()
for i in range(1,N+1):
    que.append(i)
die = 1
lst = list()
while True:

    if die % K != 0:
        x = que.popleft()
        que.append(x)
        die = die+1
    else:
        x = que.popleft()
        lst.append(x)
        die = die+1
    if len(que) == 0:
        break


print("<",end="")
for i in range(len(lst)):
    if i != len(lst)-1:
        print(lst[i],end="")
        print(", ", end="")
    else:
        print(lst[i],end="")

print(">",end="")