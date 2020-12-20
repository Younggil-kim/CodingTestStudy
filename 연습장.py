from queue import PriorityQueue

que = PriorityQueue()
que.put((1,1))
que.put((1,-1))
que.put((1,1))

print(que.get_nowait())