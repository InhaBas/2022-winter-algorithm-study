# 1546 - 평균 한번 수정
# import numpy
import statistics

n = int(input())

lst = list(map(int, input().split())) #lst에 점수를 넣는 단계

maxx = max(lst) # 어차피 한번 입력한 순간 그 최댓값이 정해지기 떄문에 미리 설정을 해 두어야 함.

for i in range(len(lst)):  # 점수조작을 하는 단계
    lst[i] = (lst[i] / maxx) * 100 # i 값 위치의 값을 변경후 대체.

# print(numpy.mean(lst)) numpy 모듈을 이용해서 할 수도 있을 것 같습니다.

print(statistics.mean(lst))  # 파이썬에 기본으로 탑재된 statistics 라이브러리 사용. 아니면 sum 함수 등을 통해서도 가능은 할 것 같다.
