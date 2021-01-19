#문제 해석

# 수열 A가 주어질 때 , 가장 긴 증가하는 부분 수열 A를 골라라

# 가장 길이가 큰 수열을 나타내는게 아닌
# 가장 길이가 긴 수열의 길이를 나타내는것
# 따라서 앞쪽부터 돌면서, 끝에 들어가는거면 추가해주면되고
# 앞에 들어가는거면 그냥 과감히 교체해준다
# 왜냐하면 앞에 들어가는거면 교체해주기때문에 전체 길이는 안바뀌기 떄문
from bisect import bisect_left

N = int(input())
lst = list(map(int, input().split()))

result = list()

for num in lst:
    number = bisect_left(result, num)
    if number >= len(result):
        result.append(num)
    else:
        result[number] = num

print(len(result))
