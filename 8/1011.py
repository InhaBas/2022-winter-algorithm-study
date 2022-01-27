t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count마다 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance: # 이동 횟수 구할 수 있는 구문
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더하기
        if count % 2 == 0 :  # count가 2의 배수일 때
            move += 1
    print(count)