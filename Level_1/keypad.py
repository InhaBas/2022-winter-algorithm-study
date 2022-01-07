loc = {1: [0, 0], 2: [0, 1], 3: [0, 2],
       4: [1, 0], 5: [1, 1], 6: [1, 2],
       7: [2, 0], 8: [2, 1], 9: [2, 2],
       '*': [3, 0], 0: [3, 1], '#': [3, 2]}

LEFT = True
RIGHT = False

def is_left(left, right, loc_go, hand) -> bool:
    left_distance = 0
    right_distance = 0

    for i, j, k in zip(left, right, loc_go):
        left_distance += abs(i-k)
        right_distance += abs(j-k)

    if left_distance == right_distance:
        if hand == 'left':
            return True
        else:
            return False
    elif left_distance < right_distance:
        return True
    else:
        return False

def solution(numbers: list, hand: str) -> str:
    answer = ''

    left_hand = loc['*']
    right_hand = loc['#']

    for i in numbers:
        loc_go = loc[i]

        if i in [1, 4, 7]:
            answer += 'L'
            left_hand = loc_go
        elif i in [3, 6, 9]:
            answer += 'R'
            right_hand = loc_go
        else:
            if is_left(left_hand, right_hand, loc_go, hand):
                answer += 'L'
                left_hand = loc_go
            else:
                answer += 'R'
                right_hand = loc_go

    return answer