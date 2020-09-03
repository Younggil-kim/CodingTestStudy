#백준 11399

#ATM기에서 인출을 하려고 하는데 줄을 서는 순서에 따라 인출에 필요한 시간이 달라진다.
#즉 빨리 뽑는 사람이 앞에 가면 효율적으로 뽑을 수 있다

#생각
# 이는 그냥 제일 빠른사람을 앞에 두고, 기다리는 시간을 구하는 문제이다.
# 정렬을 먼저 시켜주고, 이후에 합을 구한다.

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

wait_time = 0
for i in range(N):
    wait_time = wait_time + sum(lst[:i+1])
print(wait_time)