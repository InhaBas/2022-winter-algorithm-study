# 1978 - 소수 찾기

n = int(input())

sosu = list(map(int, input().split()))  # 숫자열 입력

result = 0

for i in sosu:  # 입력된 문자열에서 하나씩 꺼내 쓰면...

    cnt = 0  # 소수 판별용 카운터, 소수는 나누어지는 값이 자기 자신 하나여야 한다!

    if i == 1:  # 1은 소수가 아니다
        pass

    for j in range(2, i + 1):  # 2부터~  sosu 안의 값 i 까지

        if i % j == 0:
            cnt += 1  # 나누어 떨어지는 값을 저장.

    if cnt == 1:  # 나누어지는 값이 자기 자신 하나라면
        result += 1  # 소수라 카운터 증가.

print(result)
