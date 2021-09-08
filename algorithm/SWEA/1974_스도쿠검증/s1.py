import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]

    ans = 1
    for i in range(9):

        # 가로
        row = [0] * 10
        for j in range(9):
            row[board[i][j]] += 1
        for k in row:
            if k == 2:
                ans = 0

        # 세로
        col = [0] * 10
        for j in range(9):
            col[board[j][i]] += 1
        for k in col:
            if k == 2:
                ans = 0

    # 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):

            square = [0] * 10
            for n in range(3):
                for m in range(3):
                    square[board[i+n][j+m]] += 1
            for k in square:
                if k == 2:
                    ans = 0

    print('#{} {}'.format(tc, ans))