# 음료수 얼려 먹기
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다.(1<=N, M<=1000)
# 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어집니다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x, y - 1)
        return True
    return False

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
result = 0

print(graph)

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

# 미로 탈출
# 첫째 줄에 두 정수 N, M (4<=N, M<=200)이 주어진다. 다음 N개의 줄에는 각각 M개의 정수
# (0 혹은 1)로 미로의 정보가 주어집니다. 각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다.
# 또한 시작칸과 마지막 칸은 항상 1입니다.
# 시작위치는 (1,1)이며 한반에 한칸씩 이동가능합니다. 괴물이 있는곳은 0 없는 부분은 1로 표시
# 탈출 출구는 (N, M) 입니다.
# 첫째 줄에 최소 이동 칸의 개수를 출력합니다.
# 거리 문제이므로 BFS를 사용합니다.
# bfs는 queue를 사용
from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))
