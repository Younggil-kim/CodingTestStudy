def solution(citations):
    result = 0
    grp = list(set(citations))
    citations.sort(reverse=True)
    grp.sort(reverse=True)
    # 정렬 후에, 인용횟수, 인용된 갯수를 저장하자
    cnt = 0
    lst = list()

    for i in grp:
        cnt += citations.count(i)
        lst.append((i, cnt))
    print(lst)
    answer = 0
    for index in lst:
        a, b = index
        result = min(a, b)
        answer = max(answer, result)
    return answer