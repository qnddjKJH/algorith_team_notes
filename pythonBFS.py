# BFS (Breadth-First Serach)
# 너비 우선 탐색, 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 큐 자료구조를 이용합니다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고
# 방문 처리합니다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 수행

from collections import deque
graph = [
    [],
    [2, 3, 8],      # 1번노드
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)