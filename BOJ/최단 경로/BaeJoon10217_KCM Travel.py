import sys


input = sys.stdin.readline
INF = int(1e9)
testCase = int(input())




for _ in range(testCase):
    N, M, K = map(int, input().split())#공항의 수 N, 총 지원비용 M, 티켓정보의 수 K
    #언제나 1번 도시이고, LA는 언제나 N번 도시
    grp = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(M):
        a,b,c,d = map(int, input().split())
        grp[a][b] = (c,d)
    for i in range(1,N+1):
        grp[i][i] = (0,0)
