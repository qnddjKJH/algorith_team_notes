# 퀵 정렬
# 기준 데이터 설정 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용
# 정렬 라이브러리의 근간이 되는 알고리즘
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(피벗=pivot) 설정
# O(N logN) - 평균, O(N^2) - 최악

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

pivot = array[0]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1

        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, left+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def python_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]        # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽

    return python_quick_sort(left_side) + [pivot] + python_quick_sort(right_side)

print(python_quick_sort(array))