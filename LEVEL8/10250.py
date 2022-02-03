t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')


    '''
    손님이 방문한 순서 N과 객실 호수의 규칙성:
    층수는 N에서 건물 층수를 나눈 나머지
    호수는 N에서 건물 층수를 나눈 몫 +1
    
    만일 N이 건물 층수의 배수인 경우
    층수는 입력받은 층수 그대로 되고 호수는 N에서 건물 층수는 나눈 몫
    '''
