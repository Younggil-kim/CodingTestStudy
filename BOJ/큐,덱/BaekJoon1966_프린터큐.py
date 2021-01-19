#백준 1966

#문제 해석
#프린터를 먼저 온 순으로 하지 않고, 중요도에 따라서 하려고 한다.
# 큐에 있는 문서 수와 중요도가 주어지면, 어떤 문서가 몇번째로 인쇄되는지 아는 것
# 첫줄에는 테스트 케이스 수
# 둘째줄에는 문서 수 N과 K번째로 인쇄되는가 M을 알려준다

# 다음줄에 N개 문서의 중요도가 주어짐
# 이후에 중요도 순으로 인쇄하고, 처음 K번째에 있던거는
# 언제 복사되는지 구하라

#생각
# 우선순위 큐 관한 문젠데
# 순서를 생각해야 하니까 처음에 받은 위치값을 두고
# 만약 제일 앞이 큰값이 아니여서 pop이 되면 -1,
# 만약 제일 앞이 큰값이여서 pop이되면 카운트 +1
# 만약에 위치값이 0인데 제일 큰값이 아니어셔 pop이 되면 큐 길이 -1 로 변경
# 만약 위치 값이 0인데 팝이되면 출력
from collections import deque

case = int(input())
for i in range(case):
    N, M = map(int,input().split())
    que = list(map(int, input().split()))
    cnt = 0
    while True:
        maximum = max(que)
        x = que.pop(0)
        if x != maximum:#x 가 최대치가 아닌 상황
            if M == 0:
                que.append(x)
                M = len(que)-1
            else:
                que.append(x)
                M = M-1
        else:# x 가 최대값인 상황
            if M == 0:#레프트팝이 최대값인데, 지금 나오는게 내가 찾는거면
                cnt = cnt+1
                print(cnt)
                break
            else:#레프트팝이 최대인데, 지금 찾는 M이 아니다.
                cnt = cnt + 1
                M = M-1