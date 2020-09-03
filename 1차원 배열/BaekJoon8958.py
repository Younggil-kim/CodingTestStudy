#백준 8958

#문제 해석
#OXOOX와 같은 OX결과가 있을 때 점수를 구하는 것
# 연속되게 O를 받으면 추가점이 1점씩 더 붙는다.
# 첫줄에는 테스트 케이스 개수, 각 테스트 케이스는 한줄, 그리고
# 테스트 케이스 받을 떄 마다 점수 출력해주기

#생각
# O를 받으면 1점 + 추가점의 형식으로, 조건문을 생성

N = int(input())

for i in range(N):
    result = input()
    add = 0
    cor = 1
    score = 0
    for j in range(len(result)):
        if result[j] == 'O':
            score = score + cor + add
            add = add + 1
        else:
            add = 0
    print(score)