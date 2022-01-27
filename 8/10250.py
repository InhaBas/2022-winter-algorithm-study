t = int(input()) # 숫자 입력받고

for i in range(t):
    h, w, n = map(int, input().split()) # 층수, 호수, 손님 방문 순서
    num = n//h + 1 # 고객의 층
    floor = n % h # 각층의 방번호
    if n % h == 0:  # h의 배수이면
        num = n//h
        floor = h
    print(f'{floor*100+num}')