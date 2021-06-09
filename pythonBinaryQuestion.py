# 떡볶이 떡 만들기
# 떡의 길이는 여러가지이고 절단기 높이H 를 지정하면 줄지어진 떡을 한 번에 절단합니다.
# 높이가 H보다 긴 떡은 H 위의 부분이 잘리고 낮으면 잘리지 않는다.
# 손님이 왔을때 요청한 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이
# 최댓값을 구하는 프로그램을 작성

# 문제 해결 아이디어
# 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하면 됩니다.
# 조건의 만족 여부 (예 혹은 아니오) 에 따라서 탐색 범위를 좁혀서 해결할 수 있습니다.
# 절단기의 높이는 0부터 10억까지의 정수 중 하나입니다.

# 절단기의 높이는 0부터 10억까지의 정수 중 하나입니다.
# 이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 합니다.

# 떡의 개수(N)와 요청한 길이(M) 입력
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while start <= end:  # 만나거나 엇갈리기 전까지
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid
        start = mid + 1

print(result)

# 정렬된 배열에서 특정 수의 개수 구하기
# 1초 제한, 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력
# (1 <= N <= 1,000,000), (-10^9 <= x <= 10^9)
# 둘째 줄에는 N개의 원소가 정수 형태로 공백으로 구분되어 입력
# (-10^9 <= 각 원소의 값 <= 10 ^9)
# 원소 중 x인 원소의 개수를 출력합니다. 없다면 -1을 출력
# 시간 복잡도 O(log N)
# 일반적인 선형 탐색으로는 시간초과 판정을 받을 수 있다
# 데이터가 정렬되어 있기 때문에 이진 탐색을 수행 할 수 있다.

from bisect import bisect_left, bisect_right


def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index


n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = count_by_range(arr, x, x)
if count == 0:
    print(-1)
else:
    print(count)
