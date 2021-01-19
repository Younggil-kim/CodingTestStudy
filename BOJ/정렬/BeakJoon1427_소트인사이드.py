#백준 1427 소트인사이드

#문제 해석
# 수가 주어지면 자리수를 내림차순으로 정렬할것

#생각
#리스트로 쪼갠 뒤 역정렬 후 다시 합친다

num = input()
lst = list()
for i in num:
    lst.append(i)

lst.sort(reverse=True)

result = ""
for i in lst:
    result += i
print(result)