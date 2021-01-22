# 첫 에러는 1씩올라갈때는 // +1 말고 //만 해줘야 한다는걸 생각하지 못함

def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        if speeds[0] == 1:
            days = ((100 - progresses[0]) // speeds[0])
        else:
            days = ((100 - progresses[0]) // speeds[0]+1)
        for i in range(len(speeds)):
            progresses[i] += speeds[i]*days
        j = 0
        while progresses[j] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            if len(progresses) == 0:
                break
        answer.append(cnt)
    return answer