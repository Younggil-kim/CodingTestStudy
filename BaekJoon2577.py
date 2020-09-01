#백준 2577번 숫자의 개수

# 문제 해석
# 세 개의 자연수 A,B,C를 곱한 값에서 0부터 9까지 숫자가 몇번 쓰였는지 구하는 프로그램
# A,B,C는 모두 100보다 크거나 같고, 1000보다 작은 자연수

# 생각
# 계산한 결과를 저장한 뒤, 문자열을 통해 하나씩 읽으면서 같으면 하나씩 추가

A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)

lst = list(0 for i in range(10))

for j in num:
    lst[int(j)] = lst[int(j)] + 1

for i in range(10):
    print(lst[i])

#방법 2.
#.count 사용

A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)

for i in num:
    print(num.count(i))