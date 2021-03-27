
#수열의 길이랑 수열이 무엇인지 전부 구하는 방식으로 작성했음

str1 = input()
str2 = input()

def LCS(str1,str2):
    m = len(str1)
    n = len(str2)
    b = [[0 for _ in range(m)] for i in range(n)]
    c = [[0 for _ in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[j-1] == str2[i-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = "diagonal"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "up"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "left"
    return b, c



def Print_LCS(new1,str1,m,n):
    if m == -1 or n == -1:
        return
    if new1[n][m] == "diagonal":
        Print_LCS(new1,str1,m-1,n-1)
        print(str1[m])
    elif new1[n][m] == "up":
        Print_LCS(new1,str1,m,n-1)
    elif new1[n][m] == "left":
        Print_LCS(new1,str1,m-1,n)

new1, new2 = LCS(str1,str2)
# Print_LCS(new1,str1,len(str1)-1,len(str2)-1)

print(new2[-1][-1])