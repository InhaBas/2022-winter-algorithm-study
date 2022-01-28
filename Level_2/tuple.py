def solution(s: str) -> list:
    s = s.strip('{').strip('}')
    s_list = s.split('},{')

    li = []
    for char in s_list:
        li.append(set(char.split(',')))
    li.sort()

    answer = []
    temp = list(li[0])
    answer.append(int(temp[0]))

    for index in range(1, len(li)):
        temp_set = li[index] - li[index-1]
        temp = list(temp_set)
        answer.append(int(temp[0]))

    return answer