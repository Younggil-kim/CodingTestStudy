#문제 해석

# 두 배열이 주어지는데
# 한 쪽에는 갖고있는 카드
# 다른 한쪽에는 이 카드를 몇장 들고있는지 물어보는 것
# 물어봤을때 몇장인지 알려주는 코드를 구현하세여
from bisect import bisect_right, bisect_left

N = int(input())
lstN = list(map(int, input().split()))
M = int(input())
lstM = list(map(int, input().split()))

lstN.sort()

def rangeNumber(lst, target):
    a = bisect_left(lst, target)
    b = bisect_right(lst, target)
    return b-a

for number in lstM:
    print(rangeNumber(lstN,number),end=" ")