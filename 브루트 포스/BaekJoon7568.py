#백준 7568

#생각
# 덩치가 둘다 커야 큰것.
# 그냥 조건문으로 전체 경우 다 돌리면 가능할듯

N = int(input())

lst = list()
for i in range(N):
    lst.append(input().split())

re_lst = list()
for i in range(N):
    grade = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            grade = grade + 1
    re_lst.append(grade)

for i in re_lst:
    print(i, end=' ')