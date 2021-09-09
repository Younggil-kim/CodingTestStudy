# 백준 15820
# 
a, b = map(int, input().split())

def findWrong(a,b):
    for i in range(a):
        x, y = map(int, input().split())
        if x != y:
            print("Wrong Answer")
            return
    for j in range(b):
        x, y = map(int, input().split())
        if x != y:
            print("Why Wrong!!!")
            return
    print("Accepted")

findWrong(a,b)
