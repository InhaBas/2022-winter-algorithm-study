while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)

    # https: // ooyoung.tistory.com / 45
    # try-except: 파이썬에서 구문 오류가 발생 할 때 해결할 수 있는 코드
    # 에러가 발생할 여지가 있는 경우에 try - except 구문을 이용하면 에러가 발생돼도 프로그램이 멈추지 않고 계속 진행될 수 있도록 만들 수 있다
    # 기본적인 구조는 try 구문 쪽에 에러가 발생할 가능성이 있는 코드를 작성하고 except 구문 쪽에 예외 발생 시 실행할 코드를 작성
    # 이렇게 try - except 구문으로 코드를 작성해두면 에러가 없을 때는 try 구문을 실행하고서 except를 지나쳐서 그다음 코드를 계속 진행해나가고
    # 에러가 발생하면 except 구문을 실행시킨다.
    # try-except 구문에는 추가적으로 else, finally 구문을 작성할 수도 있다.
    # else 구문에는 에러가 발생하지 않았을 때 실행할 문장을 작성하고 finally 구문에서는 무조건 실행 할 코드를 작성한다.
    # try - except - else - finally 구문으로 작성하게 되면 보다 촘촘하게 에러에 대한 대비가 가능해진다.
