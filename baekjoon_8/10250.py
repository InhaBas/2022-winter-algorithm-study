# 10250 - ACM 호텔


t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    flr = n % h
    dst = n // h + 1

    if flr == 0:
        dst -= 1
        flr = h
