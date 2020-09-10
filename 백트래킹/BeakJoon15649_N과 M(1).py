#백준 15649

#문제 해석
#첫 줄에 N과 M이 주어지고 1부터 N까지 수 중, 중복없이 M개를 고른 수열을 모두 출력하라

#백트래킹은 DFS를 기반으로  불필요한 경우를 배제하여 원하는 해답에 도달할 때 까지 탐색하는 것


N, M = map(int, input().split())

lst = list()#빈 리스트 생성
def back():
    if len(lst) == M:# 리스트 크기가 M개이면
        print(' '.join(map(str,lst)))#공백 두고 출력,
        return
    else:
        for i in range(1,N+1):# 1~N까지 반복
            if i in lst:# i가 리스트 안에 있으면
                continue# 계속 진행
            else:# 없으면
                lst.append(i)# i를 추가하고
                back()# 함수 재가동, 그러면 위에있는 for문에서 i은 있으므로 그대로, i+1는 없으므로 추가 됨
                lst.pop()#길이가 M이 되어버리면 pop을 해줘야 다음 반복문으로 돌아갈 수 있음

back()
