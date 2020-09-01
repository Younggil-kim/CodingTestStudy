#백준 2675
#
# 문제해석
# 문자열 반복, 문자열 S와 숫자 R을 입력받고
# S의 첫 문자를 R번 반복, 두번째 문자를 R번반복으로 변경

#생각
#문자열처리를 통해서 그냥 단순하게 곱하고 더한다

case = int(input())
for i in range(case):
    number, string = input().split()
    lenth = len(string)
    result = str()
    for j in range(len(string)):
        result = result + string[j]*int(number)
    print(result)