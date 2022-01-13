# 10952 번 문제.

import sys

while True:

    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break

    print(f"{a} + {b} = {a + b}")  # f-string을 통해 문자열을 만들었습니다. 좀 더 익숙해지도록 하겠습니다!
