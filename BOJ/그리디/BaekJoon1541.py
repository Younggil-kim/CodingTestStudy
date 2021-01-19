#백준 1541번

#문제 해석
#길이가 최대 50인 식이 있는데, 괄호를 적절히 쳐서 최소값으로 만들어라

#생각
#최소값이 되기 위한 조건은
#제일 처음 -가 나온 뒤에 (를 붙이고, 다음 마이너스가 나오는 앞에 괄호를 닫는다.
#그러니까 플래그를 세워서 - 발견시 -뒤에 (를 열고, -가 나올때까지 가다가 나오면 - 앞에서 닫고, 다시 뒤에서 연다
#
string = input()

result = "("

for i in string:
    if i == '-':
        result = result + ")-("
    else:
        result = result + i
result = result + ")"

final_result = eval(result)
print(result)
print(final_result)

# 나는 이게 왜 런타임 에러가 뜨는지 모르겠다.
# >> 찾아보니까, 문제 조건에는 0으로 숫자가 시작할 수 있다고 했는데
# >> eval은 012는 12로 인식하지 못한다. 따라서 런타임 에러가 난것.
# 위 방법은 틀린 방법.

# 다시 푼 방법.
# - 로 나누고, +로 나눈뒤에, 첫 원소는 무조건 더해주고, 나머지는 빼주면 된다.
lst = list(input().split("-"))
len_lst = len(lst)
result = 0
for i in range(len_lst):
    if "+" in lst[i]:
        lst[i] = lst[i].split("+")

for j in range(len(lst)):
    if j == 0:
        if type(lst[0]) is str:
            result = result + int(lst[0])
        else:
            for i in lst[0]:
                result = result + int(i)
    else:
        if type(lst[j]) is str:
            result = result - int(lst[j])
        else:
            for i in lst[j]:
                result = result - int(i)

print(result)