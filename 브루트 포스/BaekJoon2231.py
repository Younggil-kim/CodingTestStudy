#백준 2231

#분해합
#256의 분해합은 245 + 2 +4+ 5 이다. 따라서 245는 생성자가된다
#이렇게 N이 주어졌을때 가장 작은 N을 구하라

def dis_sum(N):
    M = str(N)
    result = 0
    for i in M:
        result = result + int(i)
    result = result + N
    return result

N = int(input())

min_N = N
for i in range(N):
    max_N = N-i
    if dis_sum(max_N) == N:
        min_N = min(max_N,min_N)
if min_N == N:
    print("0")
else:
    print(min_N)