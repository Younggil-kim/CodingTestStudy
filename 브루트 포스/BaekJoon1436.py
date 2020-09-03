#백준 1436

#생각
#단순하게 666부터 1씩올려가고, 문자열 처리로 666이 있으면 N을 빼자

N = int(input())
first = 666
while N != 0:
    if '666' in str(first):
        N = N-1
        if N == 0:
            break
    first = first + 1
print(first)