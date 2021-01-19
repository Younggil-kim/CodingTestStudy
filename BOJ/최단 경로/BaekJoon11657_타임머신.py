import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())

def bf(start):
    table[start] = 0
    for i in range(N):#모든 노드에 대해
        for j in range(M):#모든 간선에 대해
            cur = grp[j][0]
            nextNode = grp[j][1]
            cost = grp[j][2]
            if table[cur] != INF and table[nextNode] > table[cur] + cost:#마지막 조건에서 이게 갱신이 되어버리면 사이클이란 소리
                table[nextNode] = table[cur] + cost#왜냐면 이미 다 채워진 상황인데, 업데이트가 되어버린단 소리니까.
                if i == N-1:
                    return True
    return False


grp = []
table = [INF]*(N+1)
start = 1
for _ in range(M):
    a,b,c = map(int, input().split())
    grp.append((a,b,c))

infCycle = bf(start)

if infCycle:
    print(-1)
else:
    for i in range(2,N+1):
        if table[i] == INF:
            print(-1)
        else:
            print(table[i])