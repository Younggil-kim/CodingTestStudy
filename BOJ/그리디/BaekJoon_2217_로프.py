#문제 해석
# N개의 로프를 병렬로 이용해서 들어올릴 수 있는 최대 중량을 구해라

#생각
#작은거부터 빼면서 최대무게의 max값을 설정해준다.

import sys

N = int(sys.stdin.readline())
lst = list()
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
max_weight = 0
for i in range(N):
    max_weight = max(max_weight, (N-i)*(lst[i]))
print(max_weight)