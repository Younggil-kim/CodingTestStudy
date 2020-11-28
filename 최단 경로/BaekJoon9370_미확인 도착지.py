import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

testCase = int(input())


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

for i in range(testCase):
    n,m,t = map(int, input().split())#n, m, t 각각 교차로, 도로, 목적지 후보의 개수이다
    s,g,h = map(int, input().split())# s는 예술가들의 출발지이고, g, h 지나간 도로
    grp = [[] for _ in range(n+1)]
    for i in range(m):
        a,b,d = map(int, input().split())
        grp[a].append((b, d))
        grp[b].append((a, d))
    cdd = list()
    sTable = [INF]*(n+1)
    gTable = [INF]*(n+1)
    hTable = [INF]*(n+1)
    for i in range(t):
        cdd.append(int(input()))
    cddTable = [[INF for _ in range(n+1)] for i in range(t+1)]
    dijkstra(s, sTable)
    dijkstra(g, gTable)
    dijkstra(h, hTable)
    for i in range(1,t+1):
        dijkstra(cdd[i-1], cddTable[i])

    result = list()
    # print(cdd)
    # print(sTable[cdd[1]])
    # pss = sTable[g]
    # print(pss)
    # print("거치고")
    # print(gTable[cdd[1]])
    if sTable[g] > sTable[h]:
        pss = sTable[g]
        for i in range(1,t+1):
            rst = pss + gTable[cdd[i-1]]
            if rst == sTable[cdd[i-1]]:
                result.append(cdd[i-1])
    else:
        pss = sTable[h]
        for i in range(1, t + 1):
            rst = pss + hTable[cdd[i - 1]]
            if rst == sTable[cdd[i - 1]]:
                result.append(cdd[i - 1])

    result.sort()
    print(*result)