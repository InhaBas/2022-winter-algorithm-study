# 4673 - 셀프 넘버
# d(n)은 원래 숫자 + 각 자릿수의 합. 즉, 문자열의 형태로 변환하면 반복문을 통해 그 값을 쉽게 찾을 수 있다.

nums = set(range(1, 10001))  # 1~10000을 집합의 형태로 생성.
del_nums = set()  # 셀프 넘버가 아닌 수를 모아두는 집합.

for i in range(1, 10001):
    for _ in str(i):  # abc라는 숫자일때...
        i += int(_)  # abc + a + b + c의 값을 반복문으로 계산
    del_nums.add(i)  # 그 값을 셀프 넘버가 아닌 수를 모아두는 집합에 넣음.

result = sorted(nums - del_nums)  # sorted 함수로 셀프넘버가 아닌 수를 뺀 집합을 순서대로 정렬.

for i in result:  # 그 값을 순서대로 출력하는 반복문.
    print(i)
