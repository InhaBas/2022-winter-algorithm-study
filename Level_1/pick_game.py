def solution(board, moves):
    answer = 0
    arr = []
    bucket = []

    # column list 생성
    for i in range(len(board[0])):
        line = []
        for j in range(len(board)):
            if board[j][i] != 0:
                line.append(board[j][i])
        arr.append(line)

    # moves 바구니 실행
    for i in moves:
        if len(arr[i-1]) and bucket:
            temp = arr[i-1].pop(0)
            if temp == bucket[-1]:
                bucket.pop()
                answer += 2
            else:
                bucket.append(temp)
        elif len(arr[i-1]):
            temp = arr[i-1].pop(0)
            bucket.append(temp)

    return answer