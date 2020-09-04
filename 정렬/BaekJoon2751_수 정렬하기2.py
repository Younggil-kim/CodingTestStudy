#백준 2751

#리스트 범위가 1,000,000까지 이므로
#내장 sort 알고리즘으로는 시간초과가 남

#빠르게 읽어야 하니까, sys.stdin.readline()사용할 것
#이후에 정렬된 리스트에 대해서 출력해주기만 하면 끝
import sys

N = int(input())
lst = list()
for i in range(N):
    lst.append(int(sys.stdin.readline()))

for i in sorted(lst):
    print(i)