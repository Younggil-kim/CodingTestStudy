#백준 10818번 최소, 최대

#문제 분석
#N개의 정수가 주어질때, 최소, 최대를 구하는 프로그램
#첫줄에 정수 개수 N, 둘째줄에 정수가 나열됨
#최소와 최대값을 찾아 공백으로 구분해 출력

#생각
#리스트로 저장한 뒤, min, max 사용

N = int(input())
lst = map(int,input().split())
lst = list(lst)

print(min(lst),max(lst))