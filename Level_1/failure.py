def solution(N: int, stages: list) -> list:
    arr = []
    clear = 0
    for i in range(N, -1, -1):
        failure = stages.count(i + 1)
        clear += failure
        if clear:
            arr.append(failure / clear)
        else:
            arr.append(0)

    arr.reverse()

    dic = {i + 1: arr[i] for i in range(N)}
    answer = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    answer = [i for i, j in answer]

    return answer