# 4153 - 직각삼각형


while True:
    num_list = list(map(int, input().split()))

    num_list.sort()

    if sum(num_list) == 0: # 세 수가 다 0이면 = 합이 0
        break

    if num_list[0] ** 2 + num_list[1] ** 2 == num_list[2] ** 2: #피타고라스의 정리
        print('RIGHT')

    else:
        print('WRONG')
