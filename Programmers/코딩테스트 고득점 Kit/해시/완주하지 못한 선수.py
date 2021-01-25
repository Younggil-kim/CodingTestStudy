import heapq


def solution(participant, completion):
    answer = ''
    heapq.heapify(participant)
    heapq.heapify(completion)
    chk = 0
    while completion:
        a = heapq.heappop(participant)
        b = heapq.heappop(completion)
        if a != b:
            chk = 1
            answer = a
            break
    if chk == 0:
        answer = participant[0]

    return answer