# 어떤 나라에 N개의 도시가 있다.
# 도시는 도시끼리 통로가 있을수도 있고 없을 수도 있다
# 보내고자 하는 메시지가 있는 경우 다른 도시로 전보를 보내서 다른 도시로 해당 메시지 전송가능
# C 도시에서 최대한 많은 도시로 메시지를 보내고자 한다.
# 보낸 도시의 개수는 총 몇 개이며 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산

# 첫째줄 도시 N개, 통로 M개, 메시지를 보내고자 하는 도시 C
# 1 <= N <= 30,000 , 1 <= M <= 200,000, 1 <= C <= N
# 둘째줄 M+1 번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z
# X->Y 로 이어지는 통로, 메시지 전달시간 Z

# 주어지는 입력값이 둘 모두 제곱을 할 경우 상당한 입력양이므로
# 배열이 아닌 우선순위 큐를 사용하는 다익스트라 알고리즘을 사용
import heapq

INF = int(1e9)
n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


# 직접 생각하면서 짜봄
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 방문 확인
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

count = 0
max_dist = 0
for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)

# 시작 노드 제외해야 하므로 count - 1 이다
print(count - 1, max_dist)


# 미래 도시
# 1번 부터 N번까지의 회사가 존재
# 회사끼지는 양방향으로 연결되어있다
# 공중 미래 도시에서 특정 회사와 다른 회사가 도로로 연결되어 있다면, 정확히 1만큼의 시간으로 이동
# A회사원은 1번 회사에 위치 소개팅의 상대는 K번 회사에 존재한다.
# X번 회사에 물건을 팔기전 소개팅 상대의 회사를 찾아가 함께 커피를 마실 예정이다.
# 따라서, 1번 회사에서 출발 K번 회사를 방문한 뒤 X번 회사로 가는 것이 목표이다.
# 회사 사이를 이동하게 되는 최소 시간을 계산

# 입력
# 전체 회사 개수 N, 경로의 개수 M
# 1 <= N, M <= 100
# M + 1 번째 줄에는 연결된 두 회사의 번호가 공백으로 구분
# M + 2 번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다( 1 <= K <= 100)

# 출력
# 최소시간 출력
# 도달 불가능하면 -1 출력

# 다익스트라로 문제를 풀 수 있다
# 하지만 경로의 개수가 고작 100개 이하이므로 플로이드 워셜로 간단하게 구현 가능하다
# 1번 노드에서 k까지의 최단 거리 + k 에서 x까지의 최단 거리

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    # 여기서 실수 양방향이므로 양쪽다 1로 초기화 해준다.
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)

