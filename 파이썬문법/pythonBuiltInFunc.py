# 실전 유용한 표준 라이브러리

# itertools
# 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
# 특히 '순열'과 '조합' 라이브러리는 코테에서 자주 사용

# heapq
# 힙(Heap) 자료구조를 제공
# 일반적으로 우선순위 큐 기능을 구현하기 위해 사용

# bisect
# 이진 탐색(Binary Seach) 기능 제공

# collections
# 덱(deque), 카운터(Counter) 등의 유용한 자료구조 포함

# math
# 필수적인 수학적 기능 제공
# 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함


# 자주 사용되는 내장 함수
# sum(), min(), max(), eval()
# 여기서 eval() 사람의 입장에서 수식으로 표현된 식을 실제 수로 계산하여 반환한다.
result = sum([1, 2, 3, 4, 5])
print(result)
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

array = [("홍길동", 50), ("이순신", 32), ("아무새", 74)]
result = sorted(array, key=lambda a: a[1], reverse=True)
print(result)

# 순열과 조합
# itertools 라이브러리
# 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열
# -> itertools 내 permutations 라이브러리
# 조합: 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는것
# -> itertools 내 combinations 라이브러리

data = ["A", "B", "C"]

# 순열 ( 기본적으로 자기자신을 제외하고 계산 자기자신 포함 = 중복순열)
from itertools import permutations

result = list(permutations(data, 3))  # 모든 순열 구하기 data의 길이가 3이므로 모든 순열이 나온다
print(result)

# 조합 ( 자기자신 제외 자기 자신 포함 = 중복 조합
from itertools import combinations

result = list(combinations(data, 2))  # 2개로 뽑는 모든 조합
print(result)

# 중복 순열과 중복 조합

# 중복 순열 -> itertools 내 product 라이브러리
from itertools import product

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

# 중복 조합 -> itertools 내 combinations_with_replacement 라이브러리
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

# Counter
# 각 원소가 등장하는 횟수를 세는 기능 제공
# 미쵸따...
from collections import Counter

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])

print(counter["blue"])  # blue 등장 횟수
print(counter["green"])  # green 등장 횟수
print(dict(counter))  # 사전 자료형으로 반환

# GCD, LCM (최대공약수, 최소공배수)
# math 라이브러리에서 제공
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)
# // 몫 연산자이고
# lcm 함수 또한 제공하고 있다 예제에서의 gcd 사용법으로 나타낸 것이다.
# 실제로 lcm 은 gcd를 나눈것이기 때문

print(math.gcd(21, 14))
print(lcm(21, 14))
