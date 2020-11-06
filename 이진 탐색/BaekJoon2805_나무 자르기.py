#문제 해석

#랜선 자르기와 비슷한 문제
# 나무의 최대값의 중간값으로 첫 mid를 설정 해 놓고
# 이후에 맞는 높이를 찾아간다

#pypy아니면 시간초과 뜨는거같은데
#나중에 확인해봅시다.

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)

result = 0
while start <= end:
    tree = 0
    mid = (start + end)//2
    for i in lst:
        if i >= mid:
            tree = tree + (i - mid)
    if tree < M:#만약 지금 자른 나무가 설정한거보다 작으면
        #절단기 높이를 낮춰야지
        end = mid -1
    else: #만약 지금 자른 나무가 설정한것보다 크면
        # 절단기 높이를 높여야지
        # 그리고 최신화 해줘야지
        start = mid + 1
        result = mid

print(result)