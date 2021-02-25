def solution(tickets):
    t = dict()
    for tick in tickets:
        if tick[0] in t:
            t[tick[0]].append(tick[1])
        else:
            t[tick[0]] = [tick[1]]

    print(t)
    for i in t.keys():
        t[i].sort(reverse=True)
    print(t)

    start = ["ICN"]#ICN부터 시작
    answer = []#answer 초기화
    while start:#리스트가 빌 때 까지>>> 그러니까 여기 while문이 어떻게 동작하는거냐면
        # t 딕셔너리에 출발지 : 도착지 , 도착지 로 설정되어있는걸 전부 빼오는거야
        top = start[-1]#탑은 start의 제일 마지막 인덱스
        if top not in t or len(t[top]) == 0:# 만약 top이 t에 없고, t[top]에서 출발하는 티켓이 없으면
            answer.append(start.pop())#answer에 start를 추가해줌
        else:#그게 아닌경우,
            start.append(t[top][-1])#start에 t[top]에서 출발하는 알파벳 순서가 빠른거부터 집어넣음
            t[top].pop()#이후 pop해줌
    answer.reverse()

    print(answer)
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])