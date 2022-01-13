n = int(input())
num = n  # 변하는 값
count = 0  # 몇 번째 사이클인지

while True:
    a = num // 10 # 10의 자리 수
    b = num % 10 # 1의 자리 수
    c = (a + b) % 10 # 두 자리 수를 더한 값
    num = (b * 10) + c # 새로운 수
    count += 1 # 사이클 끝났으므로 1을 더한다
    if (num == n):
        break

print(count)