# 혼자 풀지 못하였다.
# 어려웠던 점은 되돌아 가는 경우는 없을거라고 생각했는데
# BBAAAAB처럼 다시 되돌아 가는게 이득인 경우가 있었다.
# 이 부분을 구현하는게 어려웠음. 해답은 A를
# 코드 참고 https://jgrammer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1

def solution(name):
    list = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]

    answer = 0
    locat = 0

    while 1:

        answer += list[locat]

        list[locat] = 0

        if sum(list) == 0: break#전부 왔다갔다 할 때 까지를 체크하기 위함

        left = 1
        right = 1
        print(list, locat)
        while list[locat + right] == 0:#A가 어디까지 연속해서 나오는지 찾는거
            right += 1
            print("rightA", right)

        while list[locat - left] == 0:#마찬가지 A가 어디까지 연속해서 나오는지 찾는데, 왼쪽으로 돌면서,
            left += 1#방문한 지점을 0으로 만들어주기때문에 되돌아 가는 경우를 막아버림
            print("leftA", left)

        if left >= right:
            locat += right
            answer += right

        else:
            locat -= left
            answer += left

    return answer
print(solution("JEROEN"))