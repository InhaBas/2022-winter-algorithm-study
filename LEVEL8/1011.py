t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때,
            move += 1
    print(count)

'''
^^....
세상엔 똑똑한 사람이 많다.... ^^^^^
난 언제 똑똑해지나~~~

https://ooyoung.tistory.com/91
여기 참고했습니다...

'''
