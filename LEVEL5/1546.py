n = int(input())
score = list(map(int, input().split())) # input 개수를 지정해 주어야 한다고 생각했는데, 사실 그럴 필요가 없었화
maxScore = max(score)

newAvg = (sum(score) / n) / maxScore * 100

print(newAvg)



