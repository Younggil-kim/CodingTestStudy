import heapq
a = ["bbc", "acd","d"]
heapq.heapify(a)
while a:
    s = heapq.heappop(a)
    print(s)