#백준 11650

#문제 해석
#2차원 좌표가 주어지는데, X가 증가하는 순으로, X가 같으면 y가 증가하는 순으로
#정렬할것

#문제 생각
# 2중 정렬을 사용하면 될 것 같다.

N = int(input())
lst = list()

for i in range(N):
    lst.append((input().split()))
for i in range(N):
    for j in range(2):
        lst[i][j] = int(lst[i][j])

lst.sort(key=lambda x:(x[0],x[1] ))

for i in range(N):
    print(lst[i][0],lst[i][1])