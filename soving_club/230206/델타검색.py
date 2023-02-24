'''
N x N 2차원 리스트가 입력됩니다.
어느 한 요소에 대하여 상,하,좌,우로 이웃한 요소와의 차의 절대값들을 구하고 이들의 합을 구하려 합니다.
예를들어, 아래 그림에서 7 값의 상하좌우로 이웃한 값는 2,12,6,8 이며 차들의 절대값의 합은 12 입니다.
NxN 리스트에 있는 모든 요소들에 대해서 위처럼 조사하여 이들을 전부 더한 총합을 구해주세요.
단, [0][0] 처럼 이웃한 요소가 2개인 값은 2개 대해서만 합을 구해줍니다.

[ 입력 ]
10개의 테스트케이스가 입력됩니다. (입력 예제에는 2개만 표시했습니다)
각 테스트 케이스마다 첫 번째 줄에는 N ( 1 <= N <= 100 )
두 번째 줄부터는 N 줄에 걸쳐 N x N 개의 정수가 입력되며 정수들은 공백으로 구분되어 입력된다.

[ 출력 ]
#과 테스트케이스 번호(1~10)을 출력후 공백과 총합을 출력한다.

입력
5
1 7 4 0 9
4 8 8 2 4
5 5 1 7 1
1 5 2 7 6
1 4 2 3 2
5
2 1 6 8 5
7 6 1 8 9
2 7 9 5 4
3 1 2 3 3
4 1 1 3 8

출력
#1 246
#2 232
#3 1352
#4 27782
#5 1246
#6 4870
#7 11708
#8 331784
#9 13129418
#10 135355682
'''

# ----------------------------------------------------------------- #
# 2023 - 02 - 24 복습

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    SUM = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nr = i + mr[k]
                nc = j + mc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] - arr[i][j] > 0: # 값이 양수이면 +
                        SUM += arr[nr][nc] - arr[i][j]
                    else:   # 값이 음수 이면 양수로 변환
                        SUM += -1 * (arr[nr][nc] - arr[i][j])
    print(f'#{tc} {SUM}')