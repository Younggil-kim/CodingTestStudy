#문제 해석

#배열이 두 개 주어 질 때, 다른 배열에 있는지 없는지 검사하는 것

N = int(input())
lstN = list(map(int, input().split()))
M = int(input())
lstM = list(map(int, input().split()))

lstN.sort()

def binary_search(lst, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if lst[mid] == target:
            print(1)
            return
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(0)
    return

for num in lstM:
    binary_search(lstN, num, 0,N-1)
