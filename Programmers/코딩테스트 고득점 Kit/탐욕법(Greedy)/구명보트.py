def solution(people, limit):#투포인터 활용
    people.sort()
    start = 0
    end = len(people)-1
    cnt = 0
    while start <= end:
        if people[start] + people[end] <= limit:#제한보다 낮아서 두명을 태울 수 있는 경우
            cnt += 1
            start += 1
            end -= 1
        elif people[start] + people[end] > limit: #제한보다 커서 한명밖에 못 태우는 경우
            cnt += 1
            end -= 1
    answer = cnt
    return answer