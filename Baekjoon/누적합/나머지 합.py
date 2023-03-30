'''
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

출력
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

예제 입력 1
5 3
1 2 3 1 2
예제 출력 1
7
'''
# https://smhope.tistory.com/380
# https://velog.io/@dev-junku/BOJ-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%A9-in-Python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
numRemainder = [0] * M

for i in range(N):
    sum += num[i]
    numRemainder[sum % M] += 1
    # print(numRemainder)
result = numRemainder[0]

for i in numRemainder:
    result += i * (i - 1) // 2

print(result)