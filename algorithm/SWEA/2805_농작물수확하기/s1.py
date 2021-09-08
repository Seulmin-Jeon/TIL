import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):

    # 농장의 크기 N * N
    N = int(input())
    # 농장 수익 리스트
    farm = [list(input()) for _ in range(N)]

    temp = []
    for i in range(N//2): # 0 1
        temp += farm[i][N//2-i:N//2+i+1]

    temp += farm[N//2]

    for i in range(N//2+1, N): # 3 4
        temp += farm[i][i - (N//2):N-i + (N//2)]

    total = 0
    for i in temp:
        total += int(i)

    print('#{} {}'.format(tc, total))