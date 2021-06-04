# 파이썬의 기본 입출력

# input() - 한줄의 문자열을 입력 받는 함수
# map() - 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 예시
# list(map(int, input().split()))
# 먼저 입력을 받고 공백 기준으로 구분되어 원소를 받고
# 각 원소를 정수형으로 바꾸고 리스트로 바꾼다.

# 공백 기준 구분된 데이터의 개수가 많지 않다면 단순히 다음과 같이 사용
# a, b, c = map(int, input().split())
# 공백 기준으로 구분된 각 원소가 순서대로 a, b, c로 들어간다.
# 변수의 갯수보다 원소의 개수가 더 많다면 오류가 뜬다.

n = int(input())
data = list(map(int, input().split()))
# data = input().split() 하면 공백 기준으로 구분되어 리스트로 저장된다

data.sort(reverse=True)
print(data)

# 빠르게 입력 받기
# 입력을 최대한 빠르게 받아야하는 경우가 종종 있다. => 자바의 경우 버퍼리더에 해당하는 듯
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용
# 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용

import sys

data = sys.stdin.readline().rstrip().split()
print(data)

# 출력 방법
# 기본적으로 print() 사용
# 변수를 , 콤마를 이용하여 띄어쓰기로 구분하여 출력 가능
# print() 는 기본적으로 출력 이후 줄 바꿈 수행
# 원치 않다면 'end' 속성 사용
print(7, end=" ")
print(8)
print("enter")

# 파이썬은 문자열과 정수형에서 직접적인 더하기 연산이 불가
# 그래서 정수형을 문자열로 바꿔주고 나서 더하기 연산을 한다.
answer = 8
print("정답은 " + str(answer) + "입니다.")

# f-string
# 파이썬 3.6부터 사용 가능 문자열 앞에 접두사 'f' 를 붙여 사용
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있습니다.
print(f"정답은 {answer}입니다.")
# Javascript 의 ` ${} ` 와 같다


