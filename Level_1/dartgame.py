def solution(dart_result: str) -> int:
    score = []
    num = ''
    for char in dart_result:
        if char.isdigit():
            num += char
        elif char == 'S':
            score.append(int(num))
            num = ''
        elif char == 'D':
            score.append(int(num) ** 2)
            num = ''
        elif char == 'T':
            score.append(int(num) ** 3)
            num = ''
        elif char == '*':
            if len(score) > 1:
                score[-2] = 2 * score[-2]
                score[-1] = 2 * score[-1]
            else:
                score[-1] = 2 * score[-1]
        else:
            score[-1] = -score[-1]

    return sum(score[:])