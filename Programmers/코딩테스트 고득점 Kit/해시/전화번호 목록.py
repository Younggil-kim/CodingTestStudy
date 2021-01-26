import heapq
def solution(phone_book):
#힙에 다 넣고, 빠지는 순서가 결국 접두사일텐데?
    heapq.heapify(phone_book)
    answer = True
    while phone_book:
        a = heapq.heappop(phone_book)
        if len(phone_book) == 0:
            break
        b = phone_book[0]
        lenA = len(a)
        if b[0:lenA] == a:
            answer = False
            break

    return answer