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

//while문은 리스트가 있고, 리스트의 탑이 i보다 작으면 리스트의 마지막 원소를 빼 준다. 이후 k를 -1해줌
//이게 왜 되냐면, 앞자리 수가 가장 큰 수가 되는게 결국 가장 큰 수 이기 때문임.
