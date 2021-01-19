def solution(answer):
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    a1, a2, a3 = 5, 8, 10
    res1, res2, res3 = 0,0,0
    for i in range(len(answer)):
        if ans1[i%a1] == answer[i]:
            res1 += 1
        if ans2[i%a2] == answer[i]:
            res2 += 1
        if ans3[i%a3] == answer[i]:
            res3 += 1
    res = [(res1,1),(res2,2), (res3,3)]
    res.sort()
    copy = [res1,res2,res3]
    cnt = copy.count(max(copy))
    result = []
    for i in range(cnt):
        result.append(res.pop()[1])
    result.sort()

    return result