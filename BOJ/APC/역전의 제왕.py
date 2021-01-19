from collections import deque
N, M = map(int,input().split())

lst = [[] for i in range(N+1)]

unfrez = [[] for i in range(N+1)]

faster = [[] for i in range(N+1)]


for i in range(M):
    #sub는 제출횟수, num은 문제번호
    #프리징 이후에 제출이 많을시 문제번호가 빠른순대로
    time, per, num, sub = input().split(' ')
    per, num, sub = int(per), int(num), int(sub)
    if int(time[0:2]) >= 3 and int(time[3:5]) > 0:
        faster[per].append((int(time[3:5]),num,sub,per))
    else:
        unfrez[per].append((int(time[0:2])*60 + int(time[3:5]) + (sub-1)*20,num,sub))
# lst.sort(key=lambda x:(x[1],x[0] ))

for i in range(1,N+1):
    faster[i].sort(key=lambda x : (x[1]))
print(faster)

public = list()
for i in range(1,N+1):
    if len(faster[i]) > 1:
        while len(faster[i]) > 1:#1보다 작거나 같을때까지 팝
           public.append(faster[i].pop(0))
#제일 문제번호 빠른순으로 왔으면 정렬 시간빠른순으로
public.sort()
print(public)

#이후에 그냥 시간 빠른순으로 정렬
timer = list()
for i in range(1,N+1):
    if len(faster[i]) == 1:
        timer.append(faster[i])
timer.sort(reverse=True)
print(timer)

for i in range(len(timer)):
    public.append(timer[i][0])

print(public)
#한사람이 프리징 이후 여러번 제출시 문제번호가 빠른거부터
#원래는 시간순서대로지만
result = [] * (N+1)
print(unfrez)
for i in range(1,N+1):
    total = len(unfrez[i])
    if total == 0:
        break
    pt = 0
    for j in range(total):
        pt += unfrez[i][j][0]
    result.append((total,pt,i))

result.sort()

grade = []*(N+1)
print(result)
for i in range(1,N+1):
    grade[i] = result[i][2]

print(public)