#백준 10870

#문제 해석
#n번째 피보나치 수를 출력

def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return sequence(n-2) + sequence(n-1)

num = int(input())
print(sequence(num))