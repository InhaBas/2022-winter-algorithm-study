# 2447 - 별 찍기 5

# 어렵네요....


n = int(input()) # n은 3의 제곱으로 3, 9, 27, 81...로 입력된다.


def counting_stars(n):
    if n == 3:  # 기본적인 리스트
        return ['***', '* *', '***'] # 가장 기본이 되는 3

    stars = counting_stars(n // 3)  # 현재 단계보다 한 단계 아래의 함수 호출
    lst = []
    for star in stars: # 층을 나누기 위해 여러 번
        lst.append(star * 3) # 이전 단계 3배 출력
    for star in stars:
        lst.append(star + ' ' * (n // 3) + star)
    for star in stars:
        lst.append(star * 3)
    return lst # 결국 counting_stars 함수는 리스트를 반환한다.


print('\n'.join(counting_stars(n)))
# join 함수는 리스트의 값과 값 사이에 \n을 넣어서 하나의 문자열로 합쳐준다.
# 즉, 리스트의 첫 요소를 출력한 후 줄바꿈을 하고 두번째 요소를 출력시키는 것!
