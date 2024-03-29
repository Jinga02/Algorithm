'''
골드바흐 파티션

골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

입력
첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

출력
각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

예제 입력 1
5
6
8
10
12
100
예제 출력 1
1
1
2
1
6
'''
import sys

input = sys.stdin.readline

arr = [1] * 1000001
arr[0], arr[1] = 0, 0
for i in range(2, int(1000001 ** (0.5)) + 1):
    if arr[i] == 1:
        for j in range(i+i, 1000001, i):
            arr[j] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    cnt = 0
    for k in range((N // 2) + 1):
        if arr[k] and arr[N - k]:
            cnt += 1
    print(cnt)