import sys
sys.stdin = open('input.txt')



dr = [0, 1, 1, 1]  # 행
dc = [1, 1, 0, -1] # 열

def check(r, c):
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        cnt = 1
        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
            cnt += 1
            nr, nc = nr + dr[i], nc + dc[i]
        if cnt > 4:
            return 1
    return 0


string = ['NO', 'YES']
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                continue
            ans = check(r, c)
            if ans:
                break
        if ans:
            break

    print(string[ans])