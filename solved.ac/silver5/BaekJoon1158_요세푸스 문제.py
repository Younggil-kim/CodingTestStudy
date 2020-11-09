#문제 해석

#원에 둘러앉아있는 사람 N이 주어지고
#K번째 사람이 죽는다. 그렇게 되면 죽은사람부터 또 K씩 증가해서
#K번째 사람이 또 죽을때 죽는 수열이 오세푸스 수열이다.
#N,K주어질때 구하라

N, K = map(int, input().split())

cnt = 0
lst = [i for i in range(1,N+1)]
result = list()
index = -1

while lst:
    cnt = cnt + 1
    index = index + 1
    if index == len(lst):
        index = 0
    if cnt == K:
        result.append(lst.pop(index))
        index = index - 1
        cnt = 0

print("<" + str(result)[1:-1] + ">")
