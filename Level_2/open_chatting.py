def solution(record: list) -> list:
    command = []
    dic_command = {'Enter': "님이 들어왔습니다.", 'Leave': "님이 나갔습니다."}
    dic_id = {}
    for char in record:
        temp = char.split(' ')
        if temp[0] == 'Enter':
            command.append((temp[0], temp[1]))
            dic_id[temp[1]] = temp[2]
        elif temp[0] == 'Leave':
            command.append((temp[0], temp[1]))
        else:
            dic_id[temp[1]] = temp[2]

    return [dic_id[j] + dic_command[i] for i, j in command]