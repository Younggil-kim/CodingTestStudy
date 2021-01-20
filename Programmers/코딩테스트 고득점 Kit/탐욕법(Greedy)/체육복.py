def solution(n, lost, reserve):
    #제일 먼저 n - len(lost)이후
    #일단 lost에 있는 값이 reserve에 있으면 +1
    # 그 다음 lost를 순회하면서 -1값이 reserver에 있으면 빼오기
    #없으면? +1값으로 가기
    n -= len(lost)
    copy = lost[:]
    for i in copy:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
            n += 1
    for i in lost:
        if i - 1 in reserve:
            n += 1
            reserve.remove(i-1)
            continue
        if i + 1 in reserve:
            n += 1
            reserve.remove(i+1)
            continue
    return n