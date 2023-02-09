from pprint import pprint

'''
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

[제약 사항]
1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''


def sudoku(sl):
    for i in range(9):
        # 1부터 시작
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            # 행 검사
            # print(f'i : {i}')
            # print(f'j : {j}')
            row[sl[i][j]] += 1
            if row[sl[i][j]] == 2:
                return 0

            # 열 검사
            col[sl[j][i]] += 1
            if col[sl[j][i]] == 2:
                return 0

    # 정사각형(3행 3열) 내부 검사
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            sl_3 = [0] * 10
            for i in range(3):
                for j in range(3):
                    sl_3[sl[x + i][y + j]] += 1
                    if sl_3[sl[x + i][y + j]] == 2:
                        return 0
    return 1


T = int(input())

for tc in range(1, T + 1):
    sl = [list(map(int, input().split())) for i in range(9)]

    result = sudoku(sl)
    print(f'#{tc} {result}')