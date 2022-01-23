# 1316 - 그룹 단어 체커

a = int(input())

grp_num = 0

for i in range(a):  # a 개의 주어지는 단어에 대하여
    word = input()
    for j in range(len(word) - 1):  # -1을 안해주면 이후 인덱싱에서 범위를 넘어가는 오류가 생긴다!
        if word[j] == word[j + 1]:
            continue
        elif word[j] in word[j + 1:]:  # 이 이후에도 같은 단어가 있다면 그룹 단어가 아니다!
            break
    else:  # 단어가 이어지고, 이후에 같은 문자가 없다면
        grp_num += 1

print(grp_num)
