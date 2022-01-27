def selfn(n):   # 셀프넘버 아닌 수 찾는 함수
    n = n + sum(map(int, str(n)))
    return n


notSelf = set() # 집합 자료형 선언

for i in range(1, 10001):
    notSelf.add(selfn(i)) # 1부터 10000까지 셀프 넘버가 아닌걸 추가하면


for j in range(1, 10001):
    if j not in notSelf: # 1부터 10000까지 셀프 넘버인 것을 알 수 있음
        print(j)

