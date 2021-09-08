import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):

    '''
    N극 (위)
    1 : N극 (아래로 내려옴)
    2 : S극 (위로 올라감)
    S극 (아래)
    '''

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        N_magnet = 0
        for j in range(N):
            if board[j][i] == 1:
                N_magnet += 1
            if board[j][i] == 2 and N_magnet > 0:
                count += 1
                N_magnet = 0

    print('#{} {}'.format(tc, count))
