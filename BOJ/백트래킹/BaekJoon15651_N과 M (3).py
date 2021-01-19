#백준 15651

#문제 해석
#1과 비슷하나 뽑는 수가 중복이 되어도 된다.


N, M = map(int,input().split())

lst = list()

def back3():
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1,N+1):
            lst.append(i)
            back3()
            lst.pop()

back3()