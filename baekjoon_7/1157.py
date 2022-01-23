# 1157 - 단어 공부

wrd = input().upper()  # 어차피 출력은 대문자니깐 싹다 대문자 처리

wrd_lst = list(set(wrd))  # 입력받은 값에서 중복되는 값을 제거하고(집합) 리스트로 묶는다.

cnt_lst = [wrd.count(i) for i in wrd_lst]  # 리스트 컴프리헨션으로 중복되지 않은 각 글자가 몇 번 나왔는지 세기.

if cnt_lst.count(max(cnt_lst)) > 1:  # cnt_lst의 최댓값의 갯수를 샌 값이 1보다 크면 -> 최댓값이 중복이 된다는 뜻
    print('?')

else:  # 아니면 = 최댓값이 중복되지 않는다면
    max_num = cnt_lst.index(max(cnt_lst))  # index 함수로 최댓값의 인덱스를 찾아낸다
    print(wrd_lst[max_num]) # 그 인덱스 값을 출력
