#백준 11729 하노이탑 이동순서

#재귀함수를 이용해서 하노이탑 옮기는 간단한 문제

lst = list()
cnt = 0
def hanoi(num, frm, to, other):
    global cnt
    if num == 0:
        return
    else:
        hanoi(num-1,frm, other, to)
        lst.append((frm, to))
        cnt = cnt+1
        hanoi(num-1,other,to, frm)

N = int(input())
hanoi(N,1,3,2)
print(cnt)
for i in lst:
    print(*i)

