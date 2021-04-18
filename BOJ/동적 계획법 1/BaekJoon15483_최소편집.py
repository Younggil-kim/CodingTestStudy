str1 = input()
str2 = input()

lst = [[0 for _ in range(len(str1)+1)] for i in range(len(str2)+1)]

for j in range(0,len(str1)+1):
    lst[0][j] = j
for i in range(0,len(str2) + 1):
    lst[i][0] = i

for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if str2[i-1] == str1[j-1]:
            lst[i][j] = lst[i-1][j-1]
        else:
            lst[i][j] = min(lst[i-1][j]+1, lst[i-1][j-1]+1, lst[i][j-1]+1)
print(lst[-1][-1])
