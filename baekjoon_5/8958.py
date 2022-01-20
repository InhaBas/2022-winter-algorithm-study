# 8958 - OX퀴즈 한 번 수정
# 시작부터 구글링의 도움을 좀 받았습니다...
a = int(input())

lst = []

for i in range(a):
    asr = input()

    score = 0  # 최종 점수

    strt_score = 1  # 시작 점수 값 설정

    for i in range(len(asr)):
        if asr[i] == 'O':
            score += strt_score  # 최종점수에 점수 추가
            strt_score += 1  # 점수 1증가시킴
        else:
            strt_score = 1  # X라면 점수를 다시 1점으로 리셋

    lst.append(score)

for i in lst:  # 점수 출력(한번에) 한번에 출력할 게 아니라면 위 for문 안에 lst대신 print(score)문 하나만 넣어주면 될 거 같습니다.
    print(lst_2[i])
