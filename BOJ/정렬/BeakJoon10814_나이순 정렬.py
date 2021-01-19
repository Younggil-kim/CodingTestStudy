#백준 10814

#문제 해석
#나이가 증가하는 순으로, 같으면 먼저 가입한 사람이 앞에 오는 순서

#생각
#리스트를 추가할때 순서도 같이 추가하고, 이중정렬

N = int(input())
lst = list()
for i in range(N):
    age, name= input().split()
    order = i
    lst.append((int(age), name, order))

lst.sort(key=lambda x:(x[0],x[2]))

for i in range(N):
    print(lst[i][0], lst[i][1])
