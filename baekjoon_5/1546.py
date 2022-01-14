# 1546 - 평균
# import numpy
import statistics

lst = []
lst_2 = []

n = int(input())

for i in range(n):  # 값을 입력받는 단계
    a = int(input())
    lst.append(a)

for i in range(len(lst)):  # 점수조작을 하는 단계
    t = (lst[i] / max(lst)) * 100
    lst_2.append(t)

# print(numpy.mean(lst)) numpy 모듈을 이용해서 할 수도 있을 것 같습니다.

print(statistics.mean(lst_2)) #파이썬에 기본으로 탑재된 statistics 라이브러리 사용. 아니면 sum 함수 등을 통해서도 가능은 할 것 같다.
