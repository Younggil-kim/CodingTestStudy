N = int(input())

result = list()
for i in range(N):
    result.append(list(map(int, input().split())))

if N == 1:
    print(max(result[0]))
else:
    result[1][0] += result[0][0]
    result[1][1] += result[0][0]

    for i in range(2,N):
        for j in range(len(result[i])):
            if j == 0:
                result[i][j] += result[i-1][0]
            elif j == len(result[i])-1:
                result[i][j] += result[i-1][len(result[i])-2]
            else:
                result[i][j] = max(result[i-1][j-1] + result[i][j], result[i-1][j] + result[i][j])

    print(max(result[N-1]))