from collections import deque
def solution(priorities, location):
    answer = 1
    lst = deque()
    for i in range(0, len(priorities)):
        lst.append((priorities[i], i))
    cnt = 1
    while lst:
        pri, loc = lst.popleft()

        chk = False
        for i in range(len(lst)):
            if lst[i][0] > pri:
                chk = True
        if chk is True:  # 이게 트루면 우선순위 높은게 있다는거
            # 즉 추가해줘야함
            lst.append((pri, loc))
        else:  # 이게 fail인데 원하는 값이면 출력
            if location == loc:
                answer = cnt
                break
            cnt += 1

    return answer