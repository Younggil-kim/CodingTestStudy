# 백준 1157
#
# 문제 해석
# 대소문자로 이루어진 문자열이 주어지면 가장 많이 사용된 알파벳을 구하는 문제
# 가장많이 사용된 것을 대문자로 출력한다
# 중복인경우 ? 출력

#생각
#전부 대문자로 바꾼 다음, 26개짜리 리스트를 만들고 최고값을 뽑기
#조건문을 통해 최고값이 두개 이상이면 ?출력
#65~90 대문자 아스키

string = input()
lst = list(0 for i in range(26))
string = string.upper()
len_str = len(string)
for i in range(len_str):
    lst[ord(string[i])-65] += 1

max_lst = max(lst)
count = 0
for i in lst:
    if i == max_lst:
        count = count + 1
if count > 1:
    print("?")
else:
    print(chr(lst.index(max_lst)+65))


# 좀 더 코드를 간결화 시키기
string = input()
lst = list(0 for i in range(26))
string = string.upper()
for i in string:
    lst[ord(i)-65] += 1
max_lst = max(lst)
if lst.count(max_lst) > 1:
    print('?')
else:
    print(chr(lst.index(max_lst)+65))