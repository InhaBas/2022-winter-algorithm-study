import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# sys.stdin.readline() 사용법 관련 :
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
# input과 비교했을 때 왜 효율성이 나은지:
# https://velog.io/@gouz7514/%ED%8C%8C%EC%9D%B4%EC%8D%AC-input-vs-sys.stdin.readline

# input()과 가장 큰 차이점은 input() 은 내장 함수로 취급되는 반면 sys 에 속하는 메소드들은 file object로 취급된다.
# 즉, 사용자의 입력만을 받는 buffer를 하나 만들어 그 buffer에서 읽어들이는 것이다.
#
# input()은 더 이상 입력이 없는데도 수행될 경우 EOFerror를 뱉어내는 반면 sys.stdin.readline()은 빈 문자열을 반환한다.

