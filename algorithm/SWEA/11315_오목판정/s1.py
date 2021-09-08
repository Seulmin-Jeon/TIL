import sys
sys.stdin = open('input.txt')


di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

def check(r, c):
    for i in range(4):
        ni = r + di[i]
        nj = c + dj[i]

        count = 1
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
            count += 1
            ni = ni + di[i]
            nj = nj + dj[i]

        if count > 4:
            return 1
    return 0


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    board = [list(input()) for _ in range(N)]

    result = ['NO', 'YES']
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                continue
            ans = check(i, j)
            if ans:
                break
        if ans:
            break

    print('#{} {}'.format(tc, result[ans]))