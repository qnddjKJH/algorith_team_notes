# for 와 while 둘다 있다
# 어떤 언어든 무한 루프를 구현하는 경우는 적으니
# 항상 반복문을 탈출할 수 있는지 확인
# 특히 while문

# for문의 구조 - for 변수 in 데이터(리스트, 튜플 등)
# 첫 번째 인덱스부터 차례대로 하나씩 방문
# 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용합니다.
# 이때 range(시작 값, 끝 값 + 1) 형태로 사용
# 인자를 하나만 넣으면 자동으로 시작 값이 0이 된다.
result = 0
for i in range(1, 5):
    result += i
print(result)

# continue 키워드
# 예제 1부터 9까지의 홀수의 합
result = 0
for i in range(1, 10):
    if(i % 2 == 1):
        result += i
print(result)

# break 키워드
# 1부터 5까지의 정수 차례대로 출력
i = 1
while True:
    print("현재 i : ", i)
    if(i == 5):
        break
    i += 1

# 특정 번호의 학생은 제외하기
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}
for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")


