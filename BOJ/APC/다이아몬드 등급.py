N = int(input())
s,g,p,d = map(int, input().split())
grade = input()

result = 0
num = 0

for i in grade:
    if i == 'B':#만약 브론즈고
        if num == 0:#누적이 없으면
            result += s-1#누적금액에 29만원 합하기
            num += s-1
        else: #근데 누적이 있어
            if num >= s:#한번 달성한건 줄어들지 않음
                num = 0
            else:#누적이 실버를 넘지 않으면
                #누적 + 현재 = 실버 기준액 전까지 과금
                #s = 실버기준액 - 누적
                cur = s -1 - num
                result = result + (cur)
                num = cur
    elif i == 'S':#만약 브론즈고
        if num == 0:#누적이 없으면
            result += g-1#누적금액에 29만원 합하기
            num += g-1
        else: #근데 누적이 있어
            if num >= g:#한번 달성한건 줄어들지 않음
                num = 0
            else:
                #첫달 29만원을 질렀어
                #
                cur = g -1 - num
                result = result + (cur)
                num = cur
    elif i == 'G':#만약 브론즈고
        if num == 0:#누적이 없으면
            result += p-1#누적금액에 29만원 합하기
            num += p-1
        else: #근데 누적이 있어
            if num >= p:#한번 달성한건 줄어들지 않음
                num = 0
            else:
                cur = p -1 - num
                result = result + (cur)
                num = cur
    elif i == 'P':#만약
        if num == 0:#누적이 없으면
            result += d-1#누적금액에 29만원 합하기
            num += d-1
        else: #근데 누적이 있어
            if num >= d:#한번 달성한건 줄어들지 않음
                num = 0
            else:
                cur = d -1 - num
                result = result + (cur)
                num = cur
    elif i == 'D':
        result += d

print(result)