import sys
sys.stdin = open('input.txt')


# 오른쪽 / 오른쪽 아래 대각선 / 아래 / 왼쪽 아래 대각선
dr = [0, 1, 1, 1]  # 행
dc = [1, 1, 0, -1] # 열

# for문 돌면서 돌이 있는 좌표를 발견하면
# 그 좌표를 기준으로 네 방향으로 4개 이상 연속으로 돌이 있는지 판단하는 함수

def check(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        cnt = 1
        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
            cnt += 1
            nr = nr + dr[i]
            nc = nc + dc[i]
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

    print('#{} {}'.format(tc, string[ans]))