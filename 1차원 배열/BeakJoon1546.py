#백준 1546번

# 문제 해석
# 점수 조작을 위해, 최고점을 찾고, 나무지 점수를 X/MAX * 100으로 변경
#이후 새로운 평균을 구할 것

# 생각
# 입력은 첫줄에 과목 개수, 둘째줄에 점수
# 점수를 리스트에 저장하고, MAX 찾은 후, 나머지 변경하고 다시 평균구하기

num = int(input())
lst = map(int,input().split())
lst = list(lst)

maximum = max(lst)
for i in range(num):
    lst[i] = lst[i]*100/maximum

print(sum(lst)/len(lst))