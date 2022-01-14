n = int(input())

for i in range(n):
    oxList = input()
    score = 0
    sumScore = 0 # 총 점수
    for ox in oxList:
        if ox == 'O':
            score += 1
        else:
            score = 0 # 점수 초기화
        sumScore += score # 총 점수에 점수들 더함
    print(sumScore)