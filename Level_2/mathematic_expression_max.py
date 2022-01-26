def solution(expression: str) -> int:
    combinations = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '-', '+'],
                    ['*', '+', '-']]

    answer = []
    for comb in combinations:
        num_list = []
        operator = []
        temp = ''
        for char in expression:
            if char.isalnum():
                temp += char
            else:
                num_list.append(temp)
                operator.append(char)
                temp = ''
        num_list.append(temp)

        for op in comb:
            while op in operator:
                idx = operator.index(op)
                num_list[idx] = str(eval(num_list[idx] + op + num_list[idx + 1]))
                del num_list[idx + 1]
                del operator[idx]
        answer.append(abs(int(num_list[0])))
    return max(answer)

print(solution("100-200*300-500+20"))



