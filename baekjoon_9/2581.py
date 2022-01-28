# 2581 - 소수

m = int(input())

n = int(input())

sosu_lst = []  # 빈 리스트를 하나 생성

for i in range(m, n + 1):  # m부터 n까지
    cnt = 0  # i의 약수를 셀 카운터 생성
    for j in range(1, i + 1):  # 1부터 i 까지에 대하여
        if i % j == 0:  # 약수가 있다면
            cnt += 1  # 카운터 증가
            if cnt > 2:  # 약수가 두 개 이상이라면(1, 자기자신 이상이라면) break
                break
    if cnt == 2:  # 약수가 2개라면
        sosu_lst.append(i)  # 해당 값을 리스트에 넣는다

if len(sosu_lst) != 0:  # 리스트가 0개가 아니라면(소수가 있다면)
    print(sum(sosu_lst))  # 합 출력
    print(sosu_lst[0])  # 0번째, 즉 최솟값 출력

else:
    print('-1')
