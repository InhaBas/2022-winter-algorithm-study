# 2869 - 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())

day = 0  # 며칠이 걸릴까?

h = 0  # 올라간 높이

while h < v:
    day += 1

    h += a

    if h >= v:
        break

    h -= b

print(day)

# 이게 적은 수는 되는데, 100, 99, 1000000000 같이 큰 수에는 연산시간이 엄청나게 오래걸립니다.... 그래서 다른 방법을 찾아봤습니다.

A, B, V = map(int, input().split())

q, r = divmod(V - A, A - B)  # divmod 함수는 q에  v - a // a - b, r에 v - a % a - b 를 출력한다.  훨씬 수학적인 방법입니다.

print(q + 2) if r else print(q + 1)  # 삼항연산자로 작성, 0, 빈 리스트, 빈 튜플 등등을 모두 false로 계산하여 else가 출력된다.
