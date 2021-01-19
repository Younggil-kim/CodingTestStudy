# 백준 15652

#문제 해석
# (2)와 비슷하지만, 같아도 되는 오름차순으로 출력한다.


N, M = map(int, input().split())
lst = list()
def back4():
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1,N+1):
            if len(lst) == 0:
                lst.append(i)
                back4()
                lst.pop()
            else:
                if i >= max(lst):
                    lst.append(i)
                    back4()
                    lst.pop()
                else:
                    continue

back4()