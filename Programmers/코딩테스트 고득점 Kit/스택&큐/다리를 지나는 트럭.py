from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bdg = [0]*(1000000)
    i = 1
    cur_weight = 0
    while truck_weights:
        a =  truck_weights.popleft()
        if cur_weight + a <= weight:
            #넘지 않으면
            bdg[i+bridge_length-1] = a
            cur_weight += a
        else:
            bdg[i+bridge_length-1] = 0
            truck_weights.appendleft(a)
        i += 1
        if bdg[i-1] != 0:#지나간걸로 현재 무게 판단하는 곳
            cur_weight -= bdg[i-1]
    answer = i+bridge_length-1
    return answer