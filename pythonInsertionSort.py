# 삽입 정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
# 평균 O(n^2) 최선 O(N)
# 이미 정렬 된 경우 빠르다 (최선의 경우)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):   # 인덱스 i 부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)