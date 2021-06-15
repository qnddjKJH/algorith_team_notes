# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 '모두 계산'
# 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행
#   매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다.
# 2차원 테이블에 최단 거리 정보를 저장한다.
# 플로이드 워셜은 DP 유형에 속한다.
# 시간 복잡도는 O(N^3) 노드의 개수가 적은 상황에서 유리
# 노드와 간선이 많으면 다익스트라가 더 유리하다.

# 특정한 노드 k를 거쳐 가는 경우를 확인합니다.
#   a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사
# node[a][b] = min(node[a][b], node[a][k] + node[k][b])

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로의 거리 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    # a -> b 로 가는 비용 c => 배열에 초기화
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 앞서 말한 O(N^3) 부분이자 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range (1, n+1):
            # 플로이드 워셜 알고리즘의 점화식부분을 코드로 나타탬
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b])

print()

# 위와 같이 코드가 비교적 간단해서 보기 쉽다
# 하지만 역시나 시간 복잡도 O(N^3) 이라 개수가 적은 경우에 사용한다.
# 예로 500가지가 있다고 가정하여도 500*500*500 이라 1억이 넘는 지라 잘 생각하고 사용하여야 한다.


