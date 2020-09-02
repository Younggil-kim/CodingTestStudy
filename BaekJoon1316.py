#백준 1316

#문제 해석
#그룹단어는 문자가 연속해서 나타나는 경우이다.
#단어 N개를 입력받아 그룹단어를 출력하는 프로그램 작성

#생각
#i,j를 움직여,
#리스트를 하나 더 두고

#리스트에 아무거도 없으면 i 추가,
#리스트에 i가 있는데 j도 있으면 j False
# #4
# aba
# abab
# abcabc
# a
def is_true(string):
    result = ""
    for i in string:
        if i not in result:
            result = result + i
        else:
            if i != result[-1]:
                return False
            else:
                result = result + i

    return True
num = int(input())
count = 0
for i in range(num):
    string = input()
    if is_true(string) == True:
        count = count + 1

print(count)
