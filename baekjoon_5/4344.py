# 4344 - 평균은 넘겠지...

import statistics

num = int(input())

for i in range(num):

    score = list(map(int, input().split()))  # 첫번째에는 학생 수가 들어오므로 슬라이싱을 통해 1번째 항목부터 끝까지 평균을 구하면 될 듯하다.

    avg = statistics.mean(score[1:])

    cnt = 0

    for _ in (score[1:]):
        if _ > avg:
            cnt += 1

    per = cnt / score[0] * 100

    print(round(per, 3), '%')
