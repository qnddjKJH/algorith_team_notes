# 함수
# 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미
# 불필요한 소스코드의 반복을 줄일 수 있다.

# 내장 함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

# 함수를 사용하면 소스코드의 길이를 줄일 수 있다.
# 매개변수: 함수 내부에서 사용할 변수, 반환값: 함수에서 처리 된 결과를 반환
def add(a, b):
    return a + b


print(add(4, 7))
# a와 b 는 매개변수 a+b 는 반환값이 된다.
# 넘겨주는 파라미터를 직접 정해줄 수 있다.
# add(b=7, a=3) 이렇게 사용하면 매개변수의 순서가 달라도 상관없다.

# global 키워드
# 함수 바깥에 선언된 변수를 바로 참조하게 된다.
a = 0


def func():
    global a
    a += 1


def func2():
    a = 0
    a += 1
    print(a)


func2()

for i in range(10):
    func()
print(a)


# def func() 안에서 a가 생기는 게 아닌 func 바깥 a=0 으로 초기화된 a 변수를 참조한다.

# ????? 파이썬에서 함수는 '여러개의 반환 값들을' 가질 수 있다.
def operator(a, b):
    add_var = a + b
    substract_bar = a - b
    return add_var, substract_bar


a, b = operator(7, 3)
print(a, b)


# 오우...쉣...이 무슨...오...신기해...

# 람다 표현식
# ㅎ...교수님 수업 잘 들을걸...
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징입니다.

def add(a, b):
    return a + b


# 일반적인 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add
print((lambda a, b: a + b)(3, 7))
# 사용법 자체는 안 어려운듯
# 한번 사용하고 말 함수가 있을 경우 유용하다. 굳이 정의 할 필요가 없으니깐

# 내장 함수에서 자주 사용되는 람다 함수
# sorted나 sort 에서 많이 사용됨
array = [("홍길동", 50), ("이순신", 32), ("아무새", 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
# 어떤 원소가 들어오면 그 원소의 두번째 원소를 기준으로 정렬 한다가 의미가 된다.
print(sorted(array, key=lambda x: x[1]))
# 같은 의미

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
# a + b 를 반환하는 함수에 list1과 list2를 원소로 준다.

print(list(result))