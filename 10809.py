inp = input()
alpt = list(range(97, 123)) # 아스키코드 숫자 범위
for x in alpt:
    print(input.find(chr(x))) # find 함수 사용

# find 함수는 문자열에서만 사용 가능하고, 비슷한 함수로 index가 있음.
# index는 문자열, 리스트, 튜플과 같은 반복 가능한 iterable 자료형에서 찾는 문자의 인덱스를 반환하는 함수
# find 함수와 다른 점은 찾는 문자가 문자열 안에 포함되지 않는 경우 -1(find 함수의 반환값), index 함수는 >AttribueError로 반환