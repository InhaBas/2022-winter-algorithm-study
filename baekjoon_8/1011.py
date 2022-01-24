# 1011 - fly me to alpha centauri
# 시작과 끝의 값은 항상 1로 고정되는 것 같습니다. 시작은 1이 아니면 의미가 없고, 끝은 1이어야만 하니까요.
# 참고 - https://wlstyql.tistory.com/54  제곱수에 따른 규칙이 있군요.

import math  # 제곱근을 구하는 sqrt를 쓰기 위해서입니다.

t = int(input())

for i in range(t):
    x, y = map(int, input().split())

    minus = int(y - x)  # 이 값이 바로 목적지와 도착지 사이의 거리입니다.

    if minus <= 3:  # 3 까진 값이 입력값과 같습니다
        print(minus)

    else:
        n = int(math.sqrt(minus))  # 거리의 제곱근을 구합시다.

        if minus == n ** 2:  # 거리가 제곱수라면
            print(2 * n - 1)

        elif n ** 2 < minus <= n ** 2 + n #제곱수는 아닌데 제곱수 + 제곱근 이하의 거리라면
            print(2 * n)

        else: #제곱수 +제곱근 이상이면서 또 다른 제곱수의 이하일때
            print(2 * n + 1)