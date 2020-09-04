#백준 2750

#문제 해석
# N개의 줄에 오름차순으로 정렬한 결과를 출력하라

#단순히 sort를 사용한다.

N = int(input())
lst = list()
for i in range(N):
    lst.append(int(input()))
lst.sort()

for i in lst:
    print(i)