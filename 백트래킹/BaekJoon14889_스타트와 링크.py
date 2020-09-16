#백준 14889 문제 해석

#마찬가지 전체 경우의 수를 다 돌려야 함
#그러면 미리 2명을 뽑아서 점수를 쭉 늘려 놓고 리스트에 기준을 잡은 다음
#남은 사람으로 해야하나?

#더해주는건 결국에, 1 3 5번이 택된다고 가정하면
#1번라인에서 1 3 5 인덱스 + 3번라인에서 1 3 5 인덱스
#5번 라인에서 1 3 5 인덱스의 합이야

#결국 라인만 선택하는 경우의 수인거
# 조합이 나눠질거아냐
# 123이면 456
# 124면 356 이런식
# 그러면 스타트팀, 링크팀 리스트를 만들고
# 각 인덱스가 조합별이라고 치고
# 마지막에 스타트팀 - 링크팀의 값을 리스트로 반환한 다음
# 출력을 min()으로 해주면 될 것 같은데

# 자 그럼 조합을 뽑아보자
# 조합은 어떻게 뽑을거야
# 6개 중에서 3개 팀을 고르는 방법이야

# 3이되면 리턴, 리스트에 추가
# 123456 중에 1을 뽑고, 23456중에 2를 뽑고 3456중에 3을 뽑는 것을 재귀로 돌려야 해
# N과 M (1)을 응용하면 될 것 같아
# import sys
#
# N = int(sys.stdin.readline())
# player_lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
# start_lst = list()
# link_lst = list()
#
# start_sum = list()
# link_sum = list()
#
# balanced = list()
# for i in range(1,N+1):
#     link_lst.append(i)
#
# def team():
#     global N
#     global player_lst
#     global start_lst
#     global link_lst
#     global start_sum
#     global link_sum
#
#     if len(start_lst) == N//2:
#         start = 0
#         link = 0
#         for i in start_lst:
#             link_lst.remove(i)
#         for k in range(N//2):
#             for l in range(N//2):
#                 start = start + player_lst[start_lst[k]-1][start_lst[l]-1]
#                 link = link + player_lst[link_lst[k]-1][link_lst[l]-1]
#         start_sum.append(start)
#         link_sum.append(link)
#         del(link_lst[:])
#         for i in range(1, N + 1):
#             link_lst.append(i)
#         return
#     else:
#         for i in range(1,N+1):
#             if i in start_lst:
#                 continue
#             else:
#                 start_lst.append(i)
#                 team()
#                 start_lst.pop()
#
# team()
# for i in range(len(start_sum)):
#     balanced.append(abs(start_sum[i]-link_sum[i]))
# print(min(balanced))

# 위의 코드는 시간초과 코드, 맞는거 같은데 좀 더 효율적으로 작성해보자
# 뺴고 넣고하는 과정이 시간이 오래걸리지
# remove도 땡겨야하는거니까 시간이 오래걸려
# 리무브 대신에 쓸 수 있는건?

# 생각해보니 1~N까지 미리 저장 안해놔도
# 합은 N+1이니까 선수는 이미 결정되어 있는데?
# 인덱스에서 N+1 - (startlist인덱스) 이렇게 하면
# 잘못 생각했다. 4567뽑은 경우 반대되는 수는 1238인데, 단순 합으로 반전시키면 안됨

# 재귀로 스타트팀 먼저 뽑고
# 1~N+1까지 만들어져 있는 리스트에서 반복문을 돌며
# 스타트팀에 없으면 링크팀에 추가하는 방식
import sys

N = int(sys.stdin.readline())
player_lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
start_lst = list()


minimum = 100

full_player = list()
for i in range(1,N+1):
    full_player.append(i)
def team():
    global N
    global player_lst
    global start_lst
    global minimum
    global full_player

    if len(start_lst) == N//2:
        start = 0
        link = 0
        link_lst = list()
        for i in full_player:
            if i not in start_lst:
                link_lst.append(i)
        for k in range(N//2):
            for l in range(N//2):
                start = start + player_lst[start_lst[k]-1][start_lst[l]-1]
                link = link + player_lst[link_lst[k]-1][link_lst[l]-1]#8 - 3, 8-3 : 8-3, 8-6 : 8-3, 8-7 , 8-3 ,8-8 |||| 5,5 5,2 5,1 5,0
        minimum = min(minimum, abs(start-link))
        return
    else:
        for i in range(1,N+1):
            if i in start_lst:
                continue
            else:
                if len(start_lst)== 0:
                    start_lst.append(i)
                    team()
                    start_lst.pop()
                else:
                    if i > max(start_lst):
                        start_lst.append(i)
                        team()
                        start_lst.pop()
                    else:
                        continue

team()

print(minimum)
#pypy3로는 성공, 파이썬으로는 시간초과
#이상한곳에서 시간을 너무 오래썼다.