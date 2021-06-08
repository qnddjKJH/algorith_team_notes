# 선택 정렬
# 기준에 따라 정렬함 가장 작은 수, 가장 큰 수 중 계속해서 기준에 맞는 데이터를 선택하여 정렬
# 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보냄
# O(n^2) 이라고 작성

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_value = i
    for j in range(i + 1, len(array)):
        if array[min_value] > array[j]:
            min_value = j
    array[i], array[min_value] = array[min_value], array[i]     # 파이썬은 스왑 가능...

print(array)
