#해석

# 영문 대문자로 이루어진 두 단어가
# 같은 종류의 문자로 이루어져있거나
# 같은 문자는 같은 개수만큼 있으면 같은 구성을 갖는다고 말한다.
#DOG 와 GOD 같은 경우 같은 구성이다
# 하지만 God good은 o하나 차이가 나므로 비슷한 구성이다

#입력으로 주어진 첫 단어와 비슷한 단어를 출력하라

#생각
# 리스트로 바꿔서 set을 했는데 글자 수가 변하지 않으면 +1
# 글자 수 차이가 1이면 + 1

N = int(input())
lst = list()
for i in range(N):
    lst.append(list(input()))


num = [[0 for a in range(26)] for _ in range(N)]

for i in range(N):
    for j in range(65,91):
        if lst[i].count(chr(j)):
            num[i][j-65] = lst[i].count(chr(j))
result = 0
lst[0].sort()
for i in range(1,N):
    cnt = 0
    plg = 0
    if abs(len(lst[0]) - len(lst[i])) <= 1:
        if len(lst[0]) - len(lst[i]) == 0:#길이가 같은 경우
            lst[i].sort()
            if lst[0] == lst[i]:
                result = result + 1
            else:
                for j in range(26):
                    if abs(num[0][j] - num[i][j]) == 1:#개수가 다른게 2개
                        cnt = cnt + 1
                    elif abs(num[0][j] - num[i][j]) >= 2:
                        plg = 1
                if cnt == 2 and plg == 0:
                    result = result + 1
        else:#길이 차이가 1인경우
            for j in range(26):
                if abs(num[0][j] - num[i][j]) == 1:#개수가 다른게 2개
                    cnt = cnt + 1
                elif abs(num[0][j] - num[i][j]) >= 2:
                    plg = 1
            if cnt == 1 and plg == 0:
                result = result + 1
print(result)
# 두 개의 단어가 같은 종류의 문자로 이루어져있고,
# 같은 문자는 같은 개수만큼 있어야 함
#>> 이 조건은 sort하고, 같다했을때 TRUe면 됨

#비슷한 구성인 경우는
#한 단어에서 한 문자를 더하거나, 빼거나, 교체했을 때
#같은 구성을 가지면 됨.
# 케이스를 나누자
# 길이가 같은 경우(acv , aax)
# sort를 해 놓고 인덱스 값이 같은지 보면 될듯

# >> 단어를 하나 교체하는 경우 밖에 없음
# >> 다른게
# 전부 돌면서, 다른게 두개이상 있으면 아웃

# 첫 단어의 길이가 긴 경우 ( abxd, abc)
# >> 단어를 하나 빼는 경우 밖에 없음
# 전부 돌면서 다른게 두개 이상 있으면 아웃

# 첫 단어 길이가 짧은 경우 (a,b, abc)
# >> 단어를 하나 추가하는 경우밖에 없음
# 무조건 둘 다 같아야 성립 됨