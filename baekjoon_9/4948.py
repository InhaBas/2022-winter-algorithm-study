# 4948 - 베르트랑 공준
# 어차피 짝수는 소수가 될 수 없으니 짝수 없는 리스트를 먼저 만드는게 편하다.

nums = {i for i in range(2, 246913) if i % 2 == 1 or i == 2}

for holsu in range(3, int(246913 ** 0.5) + 1, 2):  # holsu는 3부터 시작해서 246913의 제곱근까지의 홀수들
    nums -= {i for i in range(2 * holsu, 246913, holsu) if i in nums}  # 2와 모든 홀수에서 각 수의 제곱들을 빼서 소수만 남게

while True:
    n = int(input())

    if n == 0:
        break
    result = [i for i in range(n + 1, 2 * n + 1) if i in nums]

    print(len(result))
