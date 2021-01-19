#백준 4344

#문제 해석
#테스트 케이스 개수가 주어지고, 테스트 케이스 마다,
# 각 테스트 케이스 첫줄은 학생 수, 평균 넘는 학생 비율을 소수점 셋째까지 출력

#생각
# 다 리스트에 집어넣고 1번인덱스부터 마지막까지 평균보다 큰지 안큰지 판단 후 비율 계산


case = int(input())
for i in range(case):
    lst = map(int, input().split())
    lst = list(lst)
    count = 0
    average = sum(lst[1:])/lst[0]
    for j in range(len(lst)-1):
        if lst[j+1] > average:
            count = count+1
    rate = count/lst[0]*100
    print("%0.3f%%" %rate)
