# 계수 정렬
# 특정한 조건에 부합할 때만 사용 가능하지만 '매우 빠르게 동작하는' 정렬 알고리즘
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행시간
# O(N+K) 를 보장한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")

# 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적이다
# 예 성적 나누기
# 범위차가 큰 두 가지 데이터만 있는 예시일때 최악의 경우이다

# 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(N log N)을
# 보장하도록 설계되어 있다.
