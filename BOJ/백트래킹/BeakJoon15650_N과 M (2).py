# 백준 15650

#문제 해석
#N과 M (1)과 비슷하지만
# 모든 수열은 오름차순으로 출력이 되어야 함

N ,M = map(int,input().split())

lst = list()

def back2():
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1,N+1):
            if i in lst:
                continue
            else:
                if len(lst) == 0:
                    lst.append(i)
                    back2()
                    lst.pop()
                else:
                    if i > max(lst):
                        lst.append(i)
                        back2()
                        lst.pop()
                    else:
                        continue

back2()