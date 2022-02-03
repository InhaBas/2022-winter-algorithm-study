a, b, c = map(int, input().split())

if (c - b) <= 0: # b < c로 하면 b = c인 경우를 고려하지 못하므로, 옆의 조건을 적용시켜야함
    print(-1)

else:
    n = a / (c - b)
    n += 1 # + 1을 해줘야 이익이 되는 시점임
    print(int(n)) 