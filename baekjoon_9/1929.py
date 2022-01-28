# 1929 - 소수 구하기
# 단, 에라토스테네스의 체 방법을 이용해서. 각 수의 제곱수를 전부 지워나가다 보면, 결국엔 소수만이 남는다.

m, n = map(int, input().split())

sosu_lst = [i for i in range(0, n + 1)]

for i in range(2, n + 1):  # 2부터
    if sosu_lst[i] == 0:
        pass
    if sosu_lst[i] % i == 0:
        j = 2
        while i * j <= n:
            sosu_lst[i * j] = 0  # i의 배수를 0으로 만들어준다.
            j += 1

for i in range(m, n + 1):
    if sosu_lst[i] != 0:  # 위 식을 거치면 배수들이 모두 0 이 되므로 0이 아닌 것만 출력.
        print(sosu_lst[i])
