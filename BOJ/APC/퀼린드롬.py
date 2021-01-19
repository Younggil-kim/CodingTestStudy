
string = input()
#대소문자 둘다 가능한경우 하나로 통일
dic = {'a':'A', 'B':'b', 'D':'d','Q':'q', 'e': 'E','s':'S','R' :'r','z':'Z','y':'Y',
       'N':'n', 'O':'o','P':'p','t':'T','h':'H','U':'u','I':'i','V':'v','W':'w','X':'x',
       'L':'l','M':'m'}
notStirng = "NaBCPcDQRe4FfsGgt6hjJ9KkLyz"
lenString = len(string)
check = False
#문자열 하나하나 바꾸기
for k in dic:
    string = string.replace(k, dic[k])

#바꾸고나서, 안되는거 있는지 찾기
for i in range(lenString):
    if string[i] in notStirng:
        check = True
        break

#마지막 문자열부터 돌리자

if check:
    print("-1")
else:
    if lenStringn %2 == 0:#짝수면
        result = string[0:lenString-2]
    else:
        result = string[]
    for i in range(lenString-1,0,-1):

    print(result)