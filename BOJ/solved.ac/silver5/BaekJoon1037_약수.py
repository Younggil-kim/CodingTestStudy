#문제 해석
#양수 A가 N의 약수가 되려면, N이 A의 배수이고 A가 N과 1이 아니어야한다.

# 어떤 수 N의 진짜 약수가 주어질때, N을 구하는 프로그램 작성

# 정렬한 뒤에, 제일 처음거와, 마지막거 곱하면될텐데?

import sys
N = input()
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

print(lst[0]*lst[-1])