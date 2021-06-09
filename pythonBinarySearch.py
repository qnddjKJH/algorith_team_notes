# 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩
# 확인하는 방법
# 이진 탐색: 정려로디어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
# 하는 방법
# - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.
# O(log N) 을 보장한다.


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 반대로 오늘쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


# 반복문 버전
def loof_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n - 1)
loof_result = loof_binary_search(array, target, 0, n - 1)

if result == None or loof_result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1, loof_result + 1)

# 파이썬 이진 탐색 라이브러리
# bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
# 헷갈릴 수도 있는데 인덱스 반환이 아닌 삽일할 인덱스의 위치를 반환하는것이다
# 밑에 예시에서 x=4 로 왼쪽에서 4가 처음 들어가는곳은 2다음이고
# 오른쪽에서 찾으면 8이전이다. 그래서 2와 4 번 인덱스가 결과값으로 출력됨

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 특정 범위에 속하는 데이터 개수 구하기

# 값이 left_value, right_value 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

# 파라메트릭 서치 
# 이진 탐색 문제가 나오면 파라메트릭 서치 문제가 자주 나온다
# 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법
# 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 이진 탐색을 이용하여 해결 가능