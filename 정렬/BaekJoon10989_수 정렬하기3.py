#백준 10989

#문제 해석
#단순히 정렬하는 문제,

#수 범위가 작으면, 카운팅 정렬을 사용할 것
#간단한데, 입력받은 리스트의 가장 큰 값보다 1 크게 카운트 리스트를 만들고
# 리스트 원소 값에 맞는 카운트 리스트의 인덱스에 1씩 더해줌
# 이후에 +된 값만큼 인덱스를 출력해주면 됨.
# 위 생각대로 하니까 메모리 초과가 남.

# 입력 받자마자, 그냥 카운트 리스트의 인덱스에 +1씩 더해주는 방법으로 해야 메모리 초과 안남
# 불필요하게 리스트를 하나 더 만들면 메모리 초과가 나는듯.
import sys
N = int(sys.stdin.readline())
lst = list()

count_lst = list(0 for i in range(10001))

for i in range(N):
    count_lst[int(sys.stdin.readline())] += 1

len_countlst = len(count_lst)
for i in range(len_countlst):
    for j in range(count_lst[i]):
        print(i)
