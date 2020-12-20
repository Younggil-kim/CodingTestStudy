import heapq
import sys
# 이 알고리즘이 왜 성립하냐면
# 중간값을 잘 생각해 보면됨
# 중간값은, 중간값을 기준으로 중간값보다 작은거, 큰거가 반반씩 있음
# 따라서 max힙에는 중간값보다 작거나 같은것 들을 다 넣고
# min힙에는 중간값보다 큰것들을 다 넣게되면
# 결국 max힙의 top값이 중간값이 됨
# 짝수의 경우 작은걸 선택하기 떄문에 같이 성립 됨


input = sys.stdin.readline

minheap = list()
maxheap = list()

N = int(input())
for i in range(N):
    num = int(input())
    if len(maxheap) == len(minheap):
        heapq.heappush(maxheap, (-num, num))
    else:
        heapq.heappush(minheap, num)

    #만약 최대힙의 top 값이 최소 힙의 top 값보다 크면
    #스왑하기
    if minheap and maxheap[0][1] > minheap[0]:
        a = heapq.heappop(maxheap)[1]
        b = heapq.heappop(minheap)
        heapq.heappush(maxheap, (-b,b))
        heapq.heappush(minheap, a)

    print(maxheap[0][1])