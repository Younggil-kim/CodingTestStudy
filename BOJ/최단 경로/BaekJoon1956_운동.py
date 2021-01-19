
#플루이드 워셜 > 시간초과 판정
#pypy3로 제출 시 통과 가능
import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())

grp = [[INF]*(V+1) for _ in range(V+1)]
result = [INF]*(V+1)
for i in range(E):
    a,b,c = map(int, input().split())
    grp[a][b] = c

for k in range(1,V+1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            grp[i][j] = min(grp[i][j],grp[i][k] + grp[k][j])

for i in range(1,V+1):
    result[i] = grp[i][i]
if min(result) >= INF:
    print(-1)
else:
    print(min(result))