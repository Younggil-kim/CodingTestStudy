def solution(number, k):
    lst = list()
    for i in number:
        while lst and lst[-1] < i and k >0:#lst의 top의 값이 i보다 작으면 빼줘야함
            lst.pop()
            k = k-1
        lst.append(i)
    while k > 0:
        lst.pop()
        k = k-1
    answer = "".join(lst)
            
        
    return answer
