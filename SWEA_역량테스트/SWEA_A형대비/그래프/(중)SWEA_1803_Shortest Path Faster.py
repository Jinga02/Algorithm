'''
정점의 개수가 N개이고 간선의 개수가 M개인, 가중치가 있는 무방향 그래프에서 출발 정점의 번호과 도착 정점의 번호가 주어진다.
출발 정점에서 도착 정점에 이르는 최단경로의 길이를 출력하는 프로그램을 작성하시오.
주어지는 그래프는 하나의 연결 그래프임이 보장된다.
[제약 사항]
1. 1≤N≤100,000, N-1≤M≤300,000
2. 각 간선의 가중치는 1,000,000 이하인 양의 정수

[입력]
1. 입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어진다.
2. 그 다음 줄에 정점의 개수 N과 간선의 개수 M, 출발 정점의 번호, 도착 정점의 번호가 각각 공백 1개로 구분되어 주어진다.
3. 다음 M개 줄에는 간선의 시작점과 끝점, 가중치가 순서대로 공백을 사이에 두고 주어진다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최단 경로의 길이를 출력한다.

입력
2
2 1 1 2
1 2 1
3 2 3 1
3 2 2
1 2 1

input.txt
출력
#1 1
#2 3
'''

for tc in range(1, int(input()) + 1):
    N, M, start, end = map(int, input().split())
