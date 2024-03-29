'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1
1 2 4 3
1 2 3 4
예제 입력 2
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2
3 1 2 5 4
3 1 4 2 5
예제 입력 3
1000 1 1000
999 1000
예제 출력 3
1000 999
1000 999
'''

from collections import deque


def DFS(V):
    d_visited[V] = True
    print(V, end=' ')
    for node in range(1, N + 1):
        if not d_visited[node] and graph[V][node]:
            DFS(node)


def BFS(V):
    q = deque([V])
    b_visited[V] = True
    while q:
        root = q.popleft()
        print(root, end=' ')
        for node in range(1, N + 1):
            if not b_visited[node] and graph[root][node]:
                q.append(node)
                b_visited[node] = True


N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]  # 노드와 간선 표현

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
print(graph)
d_visited = [0] * (N + 1)  # 방문 처리
b_visited = [0] * (N + 1)  # 방문 처리
DFS(V)
print()
BFS(V)

# 테스트테스트
