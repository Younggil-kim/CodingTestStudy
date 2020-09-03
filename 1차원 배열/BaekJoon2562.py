#백준 2562 최댓값

#문제 해석
#서로 다른 9개 자연수가 주어질 때, 최대값을 찾고, 몇번째인지 찾아라
#첫째줄에 최대값, 둘째줄에 몇 번째인지 출력

#생각
# 전부 받아온 뒤에 리스트에 저장한 후, 반복문으로 max와 그 수 찾기
lst = list()
for i in range(9):
    lst.append(int(input()))

for j in range(9):
    index = j
    if lst[j] == max(lst):
        break

print(max(lst))
print(index+1)