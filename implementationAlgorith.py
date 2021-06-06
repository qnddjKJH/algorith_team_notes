# 구현 (Implementaion)
# 구현이란, 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

# 문제 종류 예시
# 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적절한 라이브러리를 찾아서 사용해야 하는 문제

# 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미로 사용
# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용

# 상하좌우 문제
# 여행가 A는 N x N 크기의 정사각형 공간위에 서 있다. 이 공간은 1x1 크기의 정사각형으로 일루어
# 있다. 가장 왼쪽 위 좌표는 (1, 1) 이며 가장 오른쪽 아래는 (N, N)에 해당한다.
# 상, 하, 좌, 우 로만 이동할 수 있으며 시작 좌표는 (1, 1)
# 계획서에 따라 이동한다고 한다. 계획서는 L, R, U, D
# L 왼쪽 1칸, R 오른쪽 1칸, U 위로 1칸, D 아래로 1칸 을 나타낸다
# 공간을 벗어나는 계획은 무시한다.
space = int(input())
plan = input().split()

x = 1
y = 1

for i in plan:
    if(i == "R"):
        if(y >= space):
            continue
        y += 1
    elif(i == "L"):
        if(y <= 1):
            continue
        y -= 1
    elif(i == "U"):
        if(x <= 1):
            continue
        x -= 1
    elif(i == "D"):
        if(x >= space):
            continue
        x += 1

print(x, y)

#답안
n = int(input())
x, y  = 1, 1
plans = input().split()

move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

# 시간 문제
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 모든 시각 중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성
# 이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제입니다.
# 그러므로 완전 탐색(Brute Forcing) 문제 유형이라고 불립니다.
# (가능한 경우의 수를 모두 검사하는 탑색방법)
n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


# 왕실의 나이트
# 행복 왕국의 왕실 정원은 체스판과 같은 8x8 좌표 평면입니다. 왕실 정원의 특정한 한 칸에
# 나이트가 서 있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는
# 나갈 수 없다. 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동 가능
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# Tip. 좌표 문제에서 이동에 관한것은 이동의 좌표를 모아두면 된다. dx, dy 처럼
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

knight = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for step in knight:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 문자열 재정렬
# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을
# 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
input_string = input()
result = []
value = 0

for character in input_string:
    print(character)
    if character.isalpha():
        result.append(character)
    else:
        value += int(character)

result.sort()
if value != 0:
    result.append(str(value))

print(''.join(result))



