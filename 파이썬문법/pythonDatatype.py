# 자료형 두가지 사전, 집합

# 사전 자료형
# 키와 값 (key, value) 의 쌍을 데이터로 가지는 자료형
# 변경불가능한 자료형을 키로 사용 => 예 튜플
# 사전 자료형은 내부적으로 해시 테이블 이용 조회 및 수정 = O(1) 의 시간이 걸림
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)

if '사과' in data:
    print("사과 가짐")

# 내부 함수
# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키의 값을 출력
for key in key_list:
    print(data[key])


# 집합 자료형
# 중복을 허용하지 않음, 순서가 없다 => 자동으로 중복 제거
# 집합은 리스트 혹은 문자열을 이용해서 초기화 할 수 있다. => 이때 set() 함수 이용
# 혹은 중괄호 안에 각원소를 , 기준으로 구분하여 삽입함으로써 초기화 가능
# 데이터의 조회 및 수정에 있어 사전 자료형과 같이 O(1) 의 시간에 처리 가능
data = set([1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6])
print(data)
data = {1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6}
print(data)

# 합집합 => A | B
# 교집합 => A & B
# 차집합 => A - B
data.add(10)    # 추가
print(data)
data.update([11, 12])    # 수정
print(data)
data.remove(1)  # 제거
print(data)

# 특징
# 리스트, 튜플은 순서가 존재 인덱싱을 통해 자료형의 값을 얻음

# 사전, 집합 자료형은 순서가 없기 때문에 인덱싱을 통해 값을 얻을 수 없다
# 그러나 사전의 키(Key) 혹은 집합의 원소(Element) 이용해 O(1)의 시간 복잡도로 조회 및 수정
