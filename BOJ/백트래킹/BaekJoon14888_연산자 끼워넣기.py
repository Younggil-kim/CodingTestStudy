#백준 14888

#문제 해석
# N개로 이루어진 수열이 주어질 때
# 주어지는 연산자를 가지고 만들수 있는 최소와 최대값 출력

#결과 저장할 리스트를 만들고
# 유망성 검사는 연산자 리스트에 들어있는 횟수만큼 연산자가 나가는 경우
# 리스트에 입력을 해주고 min값을 구해준다

#순열 문제인데, 1번을 고정하고, 2번돌리고 3번돌리고 하는 식
# N과 M 문제 변형인듯

#길이가 3이 되면 계산을 계속 해주면 됨

#실패한 코드입니다, 정상 코드는 제일 아래 주석처리 안되어있음.
# import math
# N = int(input())
# lst = list(map(int, input().split()))
#
# oper = list(map(int,input().split()))#숫자는 고정이니까 연산자가 재귀가 되어야함
# oper_lst = list()
# for i in range(4):
#     while True:
#         if oper[i] == 0:
#             break
#         if i == 0:
#             oper_lst.append("+")
#             i = i - 1
#         elif i == 1:
#             oper_lst.append("-")
#             oper[i] = oper[i]-1
#         elif i == 2:
#             oper_lst.append("*")
#             oper[i] = oper[i]-1
#         elif i == 3:
#             oper_lst.append("//")
#             oper[i] = oper[i]-1
#
#
# result = list()
# def calc(str_lst):
#     string = ""
#     for i in str_lst:
#         string = string + str(i)
#
#     return eval(string)
# calc_lst = list()
# num = 0
# def operated():
#     global  num
#     global  calc_lst
#     if len(calc_lst) == 0 or len(calc_lst) == 2:
#         v = lst.pop(0)
#         calc_lst.append(v)
#         lst.append(v)
#     if num // (N-1) >= 1:
#         z = calc(calc_lst)
#         result.append(z)
#         del(calc_lst[:])
#
#     if len(result) == math.factorial(N-1):
#         return
#
#
#     if len(calc_lst) == 3:
#         x = calc(calc_lst)
#         del(calc_lst[:])
#         calc_lst.append(x)
#
#     else:
#         if len(calc_lst) == 1:# 처음 +가 들어가면 뒤에서 *가 나와주고, 그다음 *가 나오면 뒤에 +가 나와야해
#             for i in range(N-1):
#                 c = oper_lst.pop(i)
#                 calc_lst.append(c)
#                 num = num + 1
#                 operated()
#                 oper_lst.insert(i, c)
#
# operated()
# print(result)
#실패한 코드
#너무 단편적인 생각이고, 오류도 해결하지 못하겠다.
#재귀를 잘 활용해야 함.
#문제에 힌트가 나와있는것 같다.
#연산순서는 무조건 앞에서부터 계산하는게 힌트

#그럼 재귀를 어떻게 써야할까
# 모든 경우의 수를 다 돌면서
# 재귀를 쓰려면 + - * // 각각 1개씩 있다고 하면
# 1 1 1 1 에서 0 1 1 1로 재귀, 0 1 1 1에서 0 0 1 1 , 0 1 0 1, 0, 1, 1 0,으로 재귀
# 이런식으로 재귀를 해서 계산을 해 줘야 함

N = int(input())
num_lst = list(map(int,input().split()))
oper_lst = list(map(int,input().split()))
result_list = list()

def calculate(num, num_index, add, sub, multi, division):
    global N
    global result_list
    if num_index == N:
        result_list.append(num)
        return
    else:
        if add != 0:
            calculate(num + num_lst[num_index], num_index + 1,add-1,sub,multi,division)
        if sub != 0:
            calculate(num - num_lst[num_index], num_index + 1,add,sub-1,multi,division)
        if multi != 0:
            calculate(num * num_lst[num_index], num_index + 1,add,sub,multi-1,division)
        if division != 0:
            calculate(int(num / num_lst[num_index]), num_index + 1, add, sub, multi, division-1)

calculate(num_lst[0],1,oper_lst[0],oper_lst[1],oper_lst[2],oper_lst[3])
print(max(result_list))
print(min(result_list))