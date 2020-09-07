#백준 4949

#문제 해석
#긴 문자열이 주어졌는데, 괄호 짝이 다 맞는지, 문자도 균형이 맞는지

#생각
#괄호 문제와 유사하게 (를 [ 를 스택에 넣는다. 빼는데 균형 안맞으면 no
#괄호가 없어도 균형잡힌 문자열이다.

while True:
    string = input()

    if len(string) == 1 and string[0] == ".":
        break
    stack = list()
    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                stack.append(i)
                break
            if stack[-1] == "[":
                stack.append(i)
                break
            elif stack[-1] == "(":
                stack.pop(-1)
        elif i == "]":
            if len(stack) == 0:
                stack.append(i)
                break
            if stack[-1] == "(":
                stack.append(i)
                break
            elif stack[-1] == "[":
                stack.pop(-1)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")