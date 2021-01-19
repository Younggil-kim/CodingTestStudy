#백준 11047

#문제 해석
#동전을 적절히 사용해 가치의 합을 K로 만들것
#이때 동전의 최솟값을 구하는 것이 목표
#첫줄에 N종류 동전, 가치 K가 ㅈ어진다.
#둘쨰줄에 N개의 동전의 가치가 오름차순으로 주어짐.

#생각.
# 이 문제가 왜 그리디 알고리즘을 써야하나?
# 왜냐하면, 제일 가격이 낮은 동전의 배수가 큰 동전인 특별한 상황이기 떄문이다.
# 이경우에서 최솟값을 구하려면 당연히 제일 큰수 부터 빼면 된다.

N, K = map(int, input().split())
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)