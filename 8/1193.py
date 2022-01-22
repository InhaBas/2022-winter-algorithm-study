n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))

# 위의 그림을 보면 일정한 규칙이 나타남을 알 수 있다.
# 라인에 있는 분수의 개수는 1라인은 1개, 2라인은 2개, 3라인은 3개, 4라인은 4개...
# 이런 식으로 늘어감을 알 수 있다.
# 짝수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고 분모가 1씩 감소하며
# 홀수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고 분모가 1씩 늘어난다.

# https://hongcoding.tistory.com/33