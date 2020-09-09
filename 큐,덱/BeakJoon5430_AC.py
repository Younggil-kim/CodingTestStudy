#백준 5430

#문제 해석
#함수 R은 리스트 뒤집는거
# D는 첫 숫자를 버리는거
# 비어있으면 에러가남 D쓸때
# 함수는 조합해서 한번에 사용할 수 있어
# RDD는 뒤집고 처음 두개 버리는거
# 초기값과 수행 함수가 주어졌을 때, 최종 결과를 구해라

#첫줄 테스트케이스 T,
# 각 케이스 첫줄에는 함수 p가 주어짐
# 다음 줄에는 배열에 있는 수 개수 n이 주어짐
# # 그 다음 줄에는 배열형태로 들어있는 수가 주어짐
# #
# import sys
# from collections import deque
#
# case = int(sys.stdin.readline())
#
# for j in range(case):
#     func = sys.stdin.readline()
#     N = sys.stdin.readline()
#     lst = sys.stdin.readline()
#     errplg = 0
#     if len(lst) > 2:
#         if "," in lst:
#             lst = list(map(int, lst[1:-2].split(",")))
#         else:
#             lst = list(map(int, lst[1:-2].split()))
#     else:
#         lst = list()
#     for i in func:
#         if i == "R":
#             lst.reverse()
#         elif i == "D":
#             if len(lst) == 0:
#                 print("error")
#                 errplg += 1
#                 break
#             else:
#                 lst = lst[1:]
#     if errplg != 0:
#         continue
#     else:
#         print(lst)
#
# # 위 코드는 시간초과인 코드
# # R에서 효율이 안나오는거같다.
# # 뒤집는걸 실제로 뒤집은것처럼 할 수 있는 방법이 없나?
# # R 스택을 쌓을까
# # R이 안나오면 D를 앞에서부터 빼주고
# # R이 나오면 그 다음 R이 나올때까지 D를 뒤에서 빼주고
# # 다시 R이 나오면 D를 앞에서 빼준다.
# # 이렇게 하면 될거같은데
# # R플래그가 0이면 앞, 1이면 뒤, 2면 앞
# import sys
#
# case = int(sys.stdin.readline())
#
# for j in range(case):
#     func = sys.stdin.readline()
#     N = sys.stdin.readline()
#     lst = sys.stdin.readline()
#     errplg = 0
#     Rplg = 0
#     if len(lst) > 2:
#         if "," in lst:
#             lst = list(map(int, lst[1:-2].split(",")))
#         else:
#             lst = list(map(int, lst[1:-2].split()))
#     else:
#         lst = list()
#     for i in func:
#         if i == "R":
#             Rplg = Rplg + 1
#         if i == "D":
#             if len(lst) == 0:
#                 print("error")
#                 errplg = errplg + 1
#                 break
#             if Rplg % 2 == 0:
#                 lst = lst[1:]
#             else:
#                 lst.pop()
#     if errplg != 0:
#         continue
#     else:
#         print(lst)
#

# 또 시간초과
# 이번엔 뭐가 문젤까
# 실제로 리스트를 옮기지 말고
# 인덱스로 처리해놓은 다음에
# 마지막에 리스트 슬라이싱을 하는 방법은?
# 
# import sys
# 
# case = int(sys.stdin.readline())
# 
# for j in range(case):
#     func = sys.stdin.readline()
#     N = sys.stdin.readline()
#     lst = sys.stdin.readline()
#     errplg = 0
#     Rplg = 0
#     Dplg = 0
#     slice_front = 0
#     if len(lst) > 2:
#         if "," in lst:
#             lst = list(map(int, lst[1:-2].split(",")))
#         else:
#             lst = list(map(int, lst[1:-2].split()))
#     else:
#         lst = list()
#     for i in func:
#         len_lst = len(lst)
#         if i == "R":
#             Rplg = Rplg + 1
#         if i == "D":
#             Dplg = Dplg+1
#             if len_lst == 0 or Dplg > len_lst:
#                 print("error")
#                 errplg = errplg + 1
#                 break
#             if Rplg % 2 == 0:
#                 slice_front = slice_front +1
#             else:
#                 lst.pop()
#     if errplg != 0:
#         continue
#     else:
#         if Rplg %2 == 0:
#             lst = lst[slice_front:]
#             print("[",end="")
#             for i in range(len(lst)-1):
#                 print(lst[i],end="")
#                 print(",",end="")
#             print(lst[-1],end="")
#             print("]")
#         else:
#             lst.reverse()
#             print("[", end="")
#             for i in range(len(lst)-1):
#                 print(lst[i], end="")
#                 print(",", end="")
#             print(lst[-1], end="")
#             print("]")

#런타임에러가 뜸
#다시 출력부분 고쳐보자

import sys

case = int(sys.stdin.readline())

for j in range(case):
    func = sys.stdin.readline()
    N = sys.stdin.readline()
    lst = sys.stdin.readline()
    errplg = 0
    Rplg = 0
    Dplg = 0
    slice_front = 0
    if len(lst) > 2:
        if "," in lst:
            lst = list(map(int, lst[1:-2].split(",")))
        else:
            lst = list(map(int, lst[1:-2].split()))
    else:
        lst = list()
    for i in func:
        len_lst = len(lst)
        if i == "R":
            Rplg = Rplg + 1
        if i == "D":
            Dplg = Dplg+1
            if len_lst == 0 or Dplg > len_lst:
                print("error")
                errplg = errplg + 1
                break
            if Rplg % 2 == 0:
                slice_front = slice_front +1
            else:
                lst.pop()
    if errplg != 0:
        continue
    else:
        if Rplg %2 == 0:
            lst = lst[slice_front:]
        else:
            lst = lst[slice_front:]
            lst.reverse()

    print("[", end='')
    for i in range(len(lst)):
        if i == len(lst) - 1:
            print(lst[i], end = '')
        else:
            print("%s," %(lst[i]), end='')
    print("]")