X = int(input())

line = 1
while X > line: # 이부분에서 헤매서 구글링 함
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')


'''
라인에 있는 분수의 개수는 1라인은 1개, 2라인은 2개, 3라인은 3개, 4라인은 4개...씩 증가
짝수라인은 시작점에서 끝점으로 갈수록 분자는 1씩 증가, 분모는 1씩 감소
홀수라인은 분자 1씩 감소, 분모 1씩 증가


'''
