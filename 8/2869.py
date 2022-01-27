import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
day = (v - b) / (a - b)
print(math.ceil(day))

# 시간초에 걸리지 않기 위해 input 대신 sys.stdin.readline() 사용
# day = (v - b) / (a - b) 로 표현하면 당연히 정수로 딱 안떨어지고 소수로 발생
# 이를 math 모듈을 사용해서 올림 처리