# 10872 - 팩토리얼
# 재귀 - 원래의 자리로 되돌아가거나 되돌아옴, 자기 자신을 호출하는 함수.

"""
n = int(input())

t = 1

for i in range(1, n):
    t = t * (i + 1)


print(t)
"""


# 단순 for 문을 사용했을때의 방법

def fact(cnt):  # 함수의 정의
    if cnt == 0:  # cnt변수가 0이 되면
        return 1  # 1을 반환해 주자
    else:
        return cnt * fact(cnt - 1) #팩토리얼 함수는 입력된 cnt값 * 1낮은 함수의 팩토리얼 값.


print(fact(int(input())))
