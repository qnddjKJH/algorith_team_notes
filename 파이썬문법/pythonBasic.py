# 양의 정수
a = 1000
print(a)

# 음의 정수
a = -7
print(a)

# 0
a = 0
print(0)

# 소수점
a = .1
print(a)

# 지수 표현법
a = 1e9
# e 는 10을 9는 10^9 을 의미한다
print(a)
print(int(a))
# 지수 표현법을 정수로 표현

# 실수형
# IEEE754 표준에서는 실수형 4바이트, 혹은 8바이트 고정된 크기의 메모리 할당
# 컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가진다.
a = .3 + .6
print(a)
if a == .9:
    print(True)
else:
    print(False)

# 개발 과정에서 실수 값을 제대로 비교하지 못해서 원하는 결과를 얻지 못할 수 있다.
# 이럴 때 round() 함수를 이용, 이러한 방법이 권장된다.
# 반올림 함수이다. 소수 셋째 자리 반올림 123.456 => round(123.456, 2) => 123.46
# 123.456 을 소수 2째 자리 까지 출력 ( 자동으로 3째 자리서 반올림 해준다)

# 사칙연산 중 파이썬은 '/' 연산을 '실수형'으로 반환한다.
# 몫연산자가 존재 '//' 나누기 연산의 몫을 구하는 연산자이다
# 그리고... 파이썬에는 '증감연산자'가 없다!
# ++ 와 -- 가 없다!

