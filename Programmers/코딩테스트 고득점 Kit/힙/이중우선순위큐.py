import heapq
def solution(operations):
    maxanswer = []
    minanswer = []
    inscnt = 0
    popcnt = 0
    for i in operations:
        if i[0] == "I":
            heapq.heappush(maxanswer, -int(i[2:]))
            heapq.heappush(minanswer, int(i[2:]))
            inscnt += 1
        elif i == "D 1":#원래 비어있어야 하는 건데, 그게 카운트 처리가됨
            if maxanswer:#비어있지 않으면
                s =heapq.heappop(maxanswer)
                minanswer.remove(-s)
                popcnt += 1
        elif i == "D -1":
            if minanswer:
                t = heapq.heappop(minanswer)
                maxanswer.remove(-t)
                popcnt += 1
    if inscnt <= popcnt:
        answer = [0,0]
    else:
        answer = [-heapq.heappop(maxanswer), heapq.heappop(minanswer)]
    return answer