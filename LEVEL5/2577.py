a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)

for i in range(10): # 숫자 0부터 9까지므로 10번 반복
    print(num.count(str(i)))

    # count: 특정 문자열이 몇번 있는지 확인해줌. str에만 쓸 수 있으므로, 꼭 형변환 해주자
    # 참고한 사이트: https://blockdmask.tistory.com/410