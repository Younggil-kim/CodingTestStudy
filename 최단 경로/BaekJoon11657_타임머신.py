import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())

def bf(start):
    table[start] = 0
    for i in range(N):
        for j in range(M):
            cur = grp[j][0]
            nextNode = grp[j][1]
            cost = grp[j][2]
            if table[cur] != INF and table[nextNode] > table[cur] + cost:
                table[nextNode] = table[cur] + cost
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