# 3053 - 택시 기하학
from math import pi  # 파이 값을 입력

r = int(input())

normal_circle = r ** 2 * pi

taxi_circle = r ** 2 * 2

print("%.6f" % normal_circle)
print("%.6f" % taxi_circle)

# f스트링으로 소수점 6자리수까지만 표현
