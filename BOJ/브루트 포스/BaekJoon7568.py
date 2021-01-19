#백준 7568

# 2020-09-13 다시 풀었을 때
#문제 해석
#몸무게,키 의 형태로 주어지는데
#둘다 커야 덩치가 크다
# 집단이 주어질 때 덩치의 순위를 표시할 것

#생각
# 경우를 다 돌리면서 둘 다 큰 경우에만
# +1을 해 줄것

N = int(input())
lst = list()
for i in range(N):
    lst.append(input().split())


for i in range(N):
    grade = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            grade = grade + 1
    print(grade,end=" ")

















