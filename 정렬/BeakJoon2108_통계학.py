# 백준 2108 통계학

#문제 해석
# 산술평균, 중앙값, 최빈값, 범위 출력하는 문제

#생각.
# 산술 평균은 합쳐서 N으로 나누기
# 중앙값은 소트시켜서 가운데값
# 최빈값은 가장 많이 나타나는 값인데, 같으면 두번째로 작은 값
# 범위는 최대값 최소값 차이


#빈도수가 좀 헷갈렸다.
#처음 생각은 리스트를 하나 더 만들어서 set으로 중복제거 한 다음
#출력할 생각이었는데, 시간초과가 났다.

#그 다음은 딕셔너리 자료형을 사용했다.
#딕셔너리 자료형이 생각보다 활용성이 많았다.
#키 벨류값을 지정해주고, 그 값으로 sorted 해주면 정렬된 리스트가 반환된다.

#반올림 하려면 round를 사용한다.

import sys
N = int(sys.stdin.readline())

lst = list()
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
arithmetical_mean = sum(lst)/len(lst)
print("%d"%round(arithmetical_mean,0))
median = lst[N//2]#2로나눈 몫
range_lst = max(lst) - min(lst)

mode = {}#딕셔너리

for i in lst:
    if i in mode:
        mode[i] += 1
    else:
        mode[i] = 1

mode = sorted(mode.items(), key=lambda x :(x[1],-x[0]), reverse= True )
def is_mode(mode):
    if len(mode) != 1:
        if mode[0][1] == mode[1][1]:
            return mode[1][0]
        else:
            return mode[0][0]
    else:
        return mode[0][0]
print(median)
print(is_mode(mode))
print(range_lst)