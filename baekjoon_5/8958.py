# 8958 - OX퀴즈
# 시작부터 구글링의 도움을 좀 받았습니다...
a = int(input())

lst_2 = []

for i in range(a):
    asr = input()

    lst = list(asr)  # 분석하기 쉽게 리스트의 형태로 만듬.

    score = 0  # 최종 점수

    strt_score = 1  # 시작 점수 값 설정

    for i in range(len(lst)):
        if lst[i] == 'O':
            score += strt_score  # 최종점수에 점수 추가
            strt_score += 1  # 점수 1증가시킴
        else:
            strt_score = 1  # X라면 점수를 다시 1점으로 리셋

    lst_2.append(score)

for i in range(len(lst_2)):  # 점수 출력(한번에)
    print(lst_2[i])
