# 5622 - 다이얼
# 딕셔너리를 쓰면 편하게 풀리지 않을까?
dial = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}  # 딕셔너리 생성

wrd = input()

time = 0
# 여기선 구글링의 도움을 받았습니다 :( for 문 안에 for 문을 넣어 돌린다는게 약간 생각하기 어렵더라구요.
for i in wrd:  # 입력된 단어를 분해
    for j in dial.keys():  # j 로 딕셔너리의 키값을 하나씩 빼 와서
        if str(i) in j:  # wrd의 i번째 글자가 딕셔너리의 키값 j 안에 있다면...
            time += dial.get(j)  # time에 그 키 값을 더함.

print(time)
