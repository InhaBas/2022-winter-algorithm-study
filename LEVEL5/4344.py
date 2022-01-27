n = int(input())

for i in range(n):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]  # score[0]: 학생수, score[1:] 점수
    count = 0
    for sc in score[1:]:
        if sc > avg:
            count += 1  # 평균 이상인 학생 수
    rate = count / score[0] * 100
    print(f'{rate:.3f}%')

    # round로 반올림 하려 했는데, 소수점 첫째자리 밖에 안나와서 구글링 해봄.
    # round는 끝자리가 0이면 출력 하지 않는다는 사실,,,
    # format을 사용하여 반올림 하기
    # format 사용 방법 참고 사이트: https://blockdmask.tistory.com/534