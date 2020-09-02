#백준 10872

#문제 해석
#단순한 펙토리얼 문제


def factorial(num):
    if num == 1 or num== 0:
        return 1
    return num*factorial(num-1)


N = int(input())
print(factorial(N))
