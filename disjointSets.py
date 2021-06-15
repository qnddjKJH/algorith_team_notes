# 서로소 집합이란 공통 원소가 없는 두 집합입니다.
# {1, 2}와 {3, 4} 는 서로소 관계이다.
# {1, 2}와 {2, 3} 은 서로소 관계가 아니다.

# 서로소 집합 자료구조
# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
#   합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치느 연산입니다.
#   찾기(find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산입니다.
# 서로소 집합 자료구조는 합치기 찾기(Union Find) 자료구조라 불리기도 합니다.

# 여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같다.
#   1. 합집합(Union) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
#       1) A와 B의 루트 노드 A', B'를 각각 찾는다.
#       2) A'를 B'의 부모 노드로 설정한다.
#   2. 모든 합집합(Union) 연산을 처리할 때까지 1번의 과정 반복

# 연결성
# 최상위 루트노드에서 연결되어 뻗어 나간 원소들은 한 집합으로 볼 수 있다.

# 기본 구현 방법

# 특정 원소가 속한 집합을 찾기
# def find_parent(parent, x):
#     # 루트 노드를 찾을 때까지 재귀 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# - 위는 재귀적으로 구현한 초기 찾기 함수 -
# 합집합 연산이 편향되게 이루어지는 경우 찾기 함수가 비효율적으로 동작
# 최악의 경우에는 찾기 함수가 모든 노드를 다 확인하게 되어 시간 복잡도 O(V)가 된다
# 그래서 찾기 함수를 최적화하기 위한 방법으로 경로 압축(Path Compression)을 이용
# 재귀적으로 호출한뒤에 부모 테이블 값을 바로 갱신한다.
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    # 결국 한번이라도 실행하면 부모 테이블의 부모 노드값이 루트 노드로 지정된다.
    # 부모 노드들이 직접적으로 루트 노드가 된다.
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 유니온 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합", end=" ")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end=" ")
for i in range(1, v + 1):
    print(parent[i], end=" ")

