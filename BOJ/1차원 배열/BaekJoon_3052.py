#백준 3052번

# 문제 해석
# 수 10개를 입력받은후, 42로 나눈 나머지를 구한다.
# 42로 나누었을때, 서로 다른 나머지가 몇 개 있는지 출력하는것

#생각
# set 자료형을 이용, 나누고 바로 입력한 뒤, 개수 출력

result = set()
for i in range(10):
    num = int(input())
    result.add(num%42)
print(len(result))