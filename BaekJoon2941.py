#백준 2941

#문제해석
#최대 100글자 단어가 주어졌을때, 몇개의 크로아티아 알파벳인지 출력
#생각
#리스트에 단어를 집어 넣고,
#알파벳을 공백으로 바꾸고, 길이 구하기.
#replace 활용

lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()
count = 0
for i in lst:
    string = string.replace(i,' ')
print(len(string))