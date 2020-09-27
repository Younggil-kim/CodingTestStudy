#백준 1931

# 문제 해석
# N개의 회의에 대해 회의실 표를 만들려 한다
# 각 회의실 I에 대해 시작, 끝 시간이 주어지고
# 회의 시간이 겹치지 않게 하면서, 회의실 사용하는 최대 개수 찾아보자.

#첫줄에 회의의 수가 주어지고,
#둘째줄부터 회의 정보가 주어진다. 공백 사이에 두고 시작, 끝시간

#생각
#끝시간은 시작시간에 겹치면 안되고, 끝 시간과 시작시간은 같아도 됨
#그러니까 끝시간을 기준으로 먼저 끝나는거 고르고, 끝을 정렬을 시키고
# 그다음에 스타

# 그 다음 끝 시간을 배정하는데, 이 때 시작시간이 앞 시간과 겹치면 안됨
# 이런식으로 배정해주면 될듯

import sys

N = int(sys.stdin.readline())
lst = list()
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

lst.sort(key=lambda x:(x[1],x[0]))

cnt = 1
last_end_time = lst[0][1]
for i in range(0,N-1):# 시작시간이 처음의 끝시간보다 작으면 안됨
    if last_end_time <= lst[i+1][0]:
        cnt = cnt + 1
        last_end_time = lst[i+1][1]

print(cnt)



















