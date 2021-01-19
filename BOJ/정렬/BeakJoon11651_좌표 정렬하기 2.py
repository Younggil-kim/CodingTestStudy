#백준 11651

#문제 해석
#y좌표가 증가하는 순으로, 그 다음 y가 같으면 x가 증가하는 순서로 정렬

#생각
#좌표 정렬 1과 마찬가지로, 인덱스만 바꿔서 출력해준다


N = int(input())
lst = list()

for i in range(N):
    lst.append((input().split()))
for i in range(N):
    for j in range(2):
        lst[i][j] = int(lst[i][j])

lst.sort(key=lambda x:(x[1],x[0] ))

for i in range(N):
    print(lst[i][0],lst[i][1])