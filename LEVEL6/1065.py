n = int(input())

if n < 100:
    print(n) # 1부터 99까지의 수는 전부 등차수열임.
else:
    num = 99 # 100 이상의 수를 입력받으면 적어도 한수가 99개는 있는 것.
    for i in range(100, n + 1):
        han = list(map(int, str(i))) # 등차수열의 조건을 만족시키는지 보기 위해 100부터 list로 만듦.
        if han[0] - han[1] == han[1] - han[2]: # 등차 수열의 조건 만족시키는지 확인
            num += 1 # 맞으면 +1
    print(num)

