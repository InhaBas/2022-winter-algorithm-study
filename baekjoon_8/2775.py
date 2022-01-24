# 2775  - 부녀회장이 될 테야

a = int(input()) #테스트 케이스

for i in range(a):

    flr = int(input())

    hosu = int(input())  # 층수와 호수를 입력받음

    lst_hosu = [i for i in range(1, hosu + 1)]  # 1호는 1명, 2호는 2명...이렇게 거주함

    for j in range(flr): #각 층에 대해서

        for k in range(1, hosu): #1명(1호) 부터 입력된 호수까지

            lst_hosu[k] += lst_hosu[k-1] # 각 층의 전 호수를 더한 것...?

    print(lst_hosu[-1])  # 리스트의 맨 끝이 살고있는 사람들의 수


