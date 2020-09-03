#백준 1018


#생각. B가 첫 시작일때, W가 첫 시작일때 난고
#경우의수를 돌려가면서 횟수를 찾는다.

input_size = map(int, input().split())
input_size = list(input_size)

lst = list()
for i in range(input_size[0]):
    lst.append(input())

repair = list()
for i in range(input_size[0]-7):
    for j in range(input_size[1]-7):
        first_W = 0
        first_B = 0
        for l in range(i,i+8):
            for m in range(j, j+8):
                if (l + m )%2 == 0:# B가 첫 시작, W가 첫 시작 동시에 개수를 세는거야
                   if lst[l][m] != 'W':
                       first_W = first_W +1
                   if lst[l][m] != 'B':
                       first_B = first_B +1
                else:#첫 줄 시작은 W이더라고 두번째는 B니까, 이게 엇갈려서 계속 나타나, 그래서 W가 첫 시작이었더라도, 두번째줄이면 B가 첫 시작이니까 B가 아니면으로 들어가는거야
                    if lst[l][m] != 'B':
                        first_W = first_W + 1
                    if lst[l][m] != 'W':
                        first_B = first_B + 1
        repair.append(first_B)
        repair.append(first_W)

print(min(repair))
