# 10870 - 피보나치 수 5

def num(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return num(n - 2) + num(n - 1)  # 구하고자 하는 위치에서 2를 뺸 위치와 1을 뺸 위치의 합


print(num(int(input())))
