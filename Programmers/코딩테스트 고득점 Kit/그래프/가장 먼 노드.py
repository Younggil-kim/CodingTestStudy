import heapq
def solution(n, edge):
    answer = 0
    INF = int(1e9)
    table = [INF]*(n+1)
    grp = [[] for _ in range(n+1)]
    for ver in edge:
        a, b = ver
        grp[a].append((b,1))
        grp[b].append((a,1))
    def stra(start):
        lst = list()
        heapq.heappush(lst, (0, start))
        table[start] = 0
        while lst:
            cost, fin = heapq.heappop(lst)
            if table[fin] < cost:
                continue
            for i in grp[fin]:
                cst = cost + i[1]
                if cst < table[i[0]]:
                    table[i[0]] = cst
                    heapq.heappush(lst, (cst,i[0]))
    stra(1)
    print(table[1:])
    answer = table[1:].count(max(table[1:]))
    return answer