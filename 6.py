# 15596
def solve(a):
    return sum(a)

# 4673
# set의 특성은 '중복 숫자가 없다' -> 중복 제거하기 위한 필터 역할로 종종 사용 가능
# set 이용하지 않을 때(리스트형으로 받아 주고 마지막 for문을 통해 중복 여부 확인)
def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x)
    return int(n) + a
a= []
for i in range(1,10001):
    k = d(i)
    a.append(k)
for b in range(1, 10001):
    if b in a:
        pass
    else:
        print(b)

# 1065번 - 한수에 대한 개념이 이해가 안 갔음
def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i))) # 숫자를 자릿수대로 분리
        if i < 100:
            hansu_cnt += 1  # 100보다 작으면 모두 한수
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]: # 등차수열의 표현
            hansu_cnt += 1
    return hansu_cnt

num = int(input())
print(hansu(num))