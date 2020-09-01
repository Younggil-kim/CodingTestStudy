#백준 10809

#단어가 주어지고, 그 단에에서 각 알파벳이 처음 등장하는 위치를 출력
#첫글자는 0번째 위치

#생각.
#문자는 아스키코드로 숫자와 연관되어 있으니까
#26개의 리스트를 만들어 놓은 후, 그 단어의 첫 위치를 아스키코드와 연관지어
#위치를 출력해준다.
#97~122

str = input()
lst = list(-1 for j in range(26))
for i in range(len(str)):
    if lst[ord(str[i])-97] == -1:
        lst[ord(str[i])-97] = i

for i in lst:
    print(i,end=' ')