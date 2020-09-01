#백준 11720

#N개의 숫자가 공백없이 쓰여져 있을 때, 합을 출력하기
#첫줄엔 숫자의 개수, 둘째줄엔 숫자 N이 공백없이 주어짐

#생각
#문자열로 생각하고 그냥 더하면 끝

case = int(input())
num = input()
result = 0
for i in num:
    result = result + int(i)
print(result)