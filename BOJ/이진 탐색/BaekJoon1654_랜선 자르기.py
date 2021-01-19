# 문제 해석

# 0부터 최대길이까지의 중간값으로 타겟값을 정해놓고
# 이후에 몫을 게산해서 최대값이 되면 저장하고 아니면 놔두고
import sys
K, N = map(int, input().split())
lst = list()
for i in range(K):
    lst.append(int(sys.stdin.readline()))

start = 1
end = max(lst)
result = 0
while start <= end:
    maxLen = 0
    mid = (start + end)//2
    for i in range(K):
        maxLen += (lst[i] // mid)
    if maxLen < N:#만들고자 하는 횟수보다 작으면
        #수를 줄여야지
        end = mid -1
    else:#만들고자 하는 횟수보다 많거나 같으면
        #수를 높여야지
        result = mid
        start = mid + 1

print(result)