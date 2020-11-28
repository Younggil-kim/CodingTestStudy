import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
N, E = map(int, input().split())
grp = [[] for _ in range(N+1)]

for i in range(E):
    a,b,c = map(int, input().split())
    grp[a].append((b,c))
    grp[b].append((a,c))
table1 = [INF]*(N+1)
v2, v3 = map(int, input().split())
v1 = 1
table2 = [INF]*(N+1)
table3 = [INF]*(N+1)

def dijkstra(start,table):
    lst = list()
    heapq.heappush(lst, (0, start))#시작 노드
    table[start] = 0
    while lst:
        cost, fin = heapq.heappop(lst)
        if table[fin] < cost:
            continue
        for i in grp[fin]:#거쳐가는곳의 노드
            cst = cost + i[1]
            if cst < table[i[0]]:
                table[i[0]] = cst
                heapq.heappush(lst, (cst, i[0]))

dijkstra(v1, table1)
dijkstra(v2, table2)
dijkstra(v3, table3)


#1 > 2 > 3
#1 > 3 > 2
result1 = table1[v2] + table2[v3] + table3[N]
result2 = table1[v3] + table3[v2] + table2[N]

if result1 >= INF and result2 >= INF:
    print(-1)
else:
    last = min(result2,result1)
    print(last)