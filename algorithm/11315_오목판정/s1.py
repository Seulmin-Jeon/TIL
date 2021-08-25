import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
#     board = [list(input())+['.'] for _ in range(N)]
#     board.append(['.']*(N+1))
#     print(board)

N = 5
board = [['.', '.', '.', 'o', '.', '.'], ['o', 'o', 'o', 'o', 'o', '.'], ['.', '.', '.', 'o', '.', '.'], ['.', '.', '.', 'o', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]
#
#     # 가로
for i in range(N):
    row_total = 0
    for j in range(N):
        if board[i][j] == 'o' and board[i][j+1] == 'o':
            row_total += 1
            if row_total == 4 :
                result = 'YES'
                break
            else:
                result = "NO"
print(result)

    # 세로
N = 5
board = [['.', 'o', '.', 'o', 'o', '.'], ['o', 'o', '.', 'o', 'o', '.'], ['.', 'o', 'o', '.', '.', '.'], ['.', 'o', '.', '.', '.', '.'], ['.', 'o', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]

for i in range(N):
    col_total = 0
    for j in range(N):
        if board[j][i] == 'o' and board[j+1][i] == 'o':
            col_total += 1
            if col_total == 4 :
                result = 'YES'
                break
        else:
            result = 'NO'
print(result)


            # col_total = 0

            # elif board[j][i] == 'o':
            #     col_total += 1
            #     if col_total == N-1 and board[j+1][i] == 'o':
            #         result = 'YES'
            # elif board[i][j] == 'o'
            # if board[i][j]


            # else:
            #     result = 'NO'



    # print('#{} {}'.format(tc, result))