def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic.keys():
            dic[i[1]] += 1
        else:
            dic[i[1]] = 0
    for i in dic.keys():
        dic[i] += 2
    cnt = 1
    for i in dic.keys():
        cnt *= dic[i]
    cnt = cnt -1
    return cnt