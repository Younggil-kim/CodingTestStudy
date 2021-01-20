import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    if scoville[0] >= K:
        return cnt
    else:
        while True:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new = first + second*2
            cnt += 1
            heapq.heappush(scoville, new)
            if scoville[0] >= K:
                return cnt
            if len(scoville) <= 1:
                return -1