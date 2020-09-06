# 백준 1181

# 문제 해석
# 알파벳으로 이루어진 문자열을, 길이가 짧은것부터, 길이가 같으면 사전순으로 정렬

# 생각
# 같은 단어가 여러번 입력되면 한번만 출력이니까 set으로 받아들이고
# 이후, 단어 길이와 같이 추가한다음, 이중 정렬을 시행한다.
import sys

N = int(sys.stdin.readline())

lst = set()
for i in range(N):
    string = input()
    string_count = len(string)
    lst.add((string,string_count))

lst = list(lst)

lst.sort(key=lambda x:(x[1],x[0] ))


for i in range(len(lst)):
    print(lst[i][0])
