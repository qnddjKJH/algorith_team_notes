# 스택
# 입구와 출구가 동일한 형태로 스택을 시각화 할 수 있습니다.
# 선입후출의 자료구조입니다.
stack = []

# 삽입5 - 삽입2 - 삭제 - 삽입1 - 삭제 - 삽입4
stack.append(5)
stack.append(2)
stack.pop()
stack.append(1)
stack.pop()
stack.append(4)

print(stack[::-1])   # 최상단 원소부터 출력
print(stack)   # 최하단 원소부터 출력


# 큐 자료구조
# 선입선출의 자료구조
# 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 가능
# 파이썬에서 큐를 쓰기 위해서는
# collections 라이브러리에 있는 deque 를 불러와야한다.
from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(4)

print(queue)
queue.reverse()    # 역순으로 바꾸기
print(queue)


# 재귀함수(Recursive Function)
# 자기 자신을 다시 호출 하는 함수

# 팩토리얼 구현 예제
def factorial_iterative(n):
    if n <= 1:
        return 1
    return n * factorial_iterative(n - 1)
print(factorial_iterative(5))

# 유클리드 호제법 (최대공약수 계산) 예제
# 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 합니다
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, (a % b))

print(gcd(192, 162))

# 재귀 함수 유의 사항
# 모든 재귀 함수는 반복문을 이용하여 동일한 기능 구현 가능
# 다른 사람이 이해하기 어려운 형태의 코드가 될 수 있으니 신중히 사용
# 반복문에 비해 유리할 수도 있고 불리할 수도 있다
# 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
# 그래서 '스택' 을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다


