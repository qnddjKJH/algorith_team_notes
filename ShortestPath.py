# 최단 경로 문제
# 가장 짧은 경로를 찾는 알고리즘
#   한 지점에서 다른 한 지점까지의 최단 경로
#   한 지점에서 다른 모든 지점까지의 최단 경로
#   모든 지점에서 다른 모든 지점까지의 최단 경로
# 각 지점은 그래프에서 노드로 표현
# 지점 간 연결된 도로는 그래프에서 간선으로 표현

# 다익스트라 최단 경로 알고리즘 (Dijkstra)
# 특정 노드에서 출발 다른 모든 노드로 가는 최단 경로를 계싼
# 음의 간선이 없을 때 정상 작동
#   현실 세계의 도로는 음의 간선으로 표현x
# 그리디 알고리즘으로 분류
# 매 상황에서 가장 비용이 적은 노드를 선택

# 동작과정
# 출발노드 설정
# 최단 거리 테이블 초기화
# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산 최단 거리 테이블 갱신
# 위 과정 중 3번과 4번 반복

# 처리 과정 중 더 짥은 경로를 찾으면 해당 경로가 짧은 경로로 갱신한다.

# 그리디 알고리즘 : 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택 임의의 과정 반복
# 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않는다.
#   한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해
# 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장
#   완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어햐 한다.

# 다익스트라: 간단한 구현 방법
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택하기 위해 매 단계마다
# 1차원 테이블의 모든 원소를 확인(순차 탐색) 완전 탐색에 가까운 거 같다.

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정한다.

# n = 노드의 개수, m = 간선의 개수, start = 시작 노드 번호
n, m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 노드 저장 (체크)
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 로 가는 cost, c = 비용
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start]
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] = j[i]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 위 코드는 5000개 이하의 노드면 충분히 계산 가능
# 하지만 10000개 라면? 더 효율 좋은 코드를 위해 아래의 내용을 배운다.

# 우선순위 큐
# 구현하기 위해 사용하는 자료구조
# 최소 힙(min Heap), 최대 힙(max hep)
# 다양한 알고리즘에서 사용한다.
# 리스트   삽입 O(1)  삭제 O(N)
# 힙         O(logN)     O(logN)

# 파이선 힙 사용방법
import heapq
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        # 힙이 따로 있는게 아니고 (넣을 곳, 값) 으로 쓴다.
        # heapq.메소드(파라미터) 로 사용
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1, 3, 5, 7, 8, 2, 4, 6, 8, 0])
# 위는 최소 힙
# 최대 힙은 위에 코드에서 value => -value
# heapq.heappop(h) => 를 -heapq.heappop(h) 으로 바꾼다 거꾸로 넣고 거꾸로 꺼냄
print(result)

# 개선된 구현방법
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미 10억

n, m = map(int, input().split())
start = int(input())

# 여기서 0번 인덱스는 쉽게 생각하기 위해 쓰지 않는다
# distance 는 최단 거리 테이블이다. 현재값을 저장하는 곳
graph = [[] for i in range(n + 1)]
distance = [INF] * (n+1)

# 간선의 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 에서 b로 가는 비용 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정 큐에 삽입.
    heapq.heappush(q, (0, start))   # 큐 첫 번째에 최단거리 노드 (0, start) 로 들어간다.
    distance[start] = 0
    while q:    # 큐가 계속 있다면
        dist, now = heapq.heappop(q)    # pop 은 제일 먼저 들어온걸 내보낸다.
        # dist에 값이 now에 현재 노드 인덱스가 들어간다.
        # distance 는 최단 거리 테이블로 현재 값보다 작다면 갱신해준다
        # 초기에 무한으로 설정되어 있어 값이 있다면의 조건을 무시가능
        # 크거나 조건이 결국 값이 존재하지 않다도 포함됨
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]  # 현재값과 비용을 더해 최단거리 비교용 코스트를 만듬
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 현재 노드가 아닌 저장된 a->b 방향의 비용을 더한 값이므로
                # i[0]에 저장된 노드의 최단 거리 테이블에 저장한다.
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


