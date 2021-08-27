import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    '''
    상하좌우 X로 채워진 패딩값 주기
    
    이중 for문 range(N)
        for range(N)
    A 찾아서 상하좌우 1개씩 X로 바꿈
    B 찾아서 상하좌우 2개씩 X로 바꿈
    C 찾아서 상하좌우 3개씩 X로 바꿈
    
    전체 돌면서 H개수 => 답
    '''

    N = int(input())
    town = [['X'] + list(input()) + ['X'] for _ in range(N)]
    town.insert(0, ['X']*(N+2))
    town.append(['X']*(N+2))

    for i in range(N+2):
        for j in range(N+2):

            if town[i][j] == 'A':
                town[i-1][j] = 'X'
                town[i][j+1] = 'X'
                town[i+1][j] = 'X'
                town[i][j-1] = 'X'
            elif town[i][j] == 'B':
                for k in range(2):
                    town[i-1-k][j] = 'X'
                    town[i][j+1+k] = 'X'
                    town[i+1+k][j] = 'X'
                    town[i][j-1-k] = 'X'
            elif town[i][j] == 'C':
                for k in range(3):
                    town[i-1-k][j] = 'X'
                    town[i][j+1+k] = 'X'
                    town[i+1+k][j] = 'X'
                    town[i][j-1-k] = 'X'

            '''
            k = 
            if town[i][j] == 'A':
                k = 1
            if town[i][j] == 'B':
                k = 2
            if town[i][j] == 'C':
                k = 3
                
            for d in range(1, k+1):
                if 0 <= j-d:
                    town[i][j-d] = 'X'
                if j+d < N:
                    town[i][j+d] = 'X'
                if 0 <= i-d:
                    
                if i+d < N:
            '''

    cnt = 0
    for i in range(N+2):
        for j in range(N+2):
            if town[i][j] == 'H':
                cnt += 1
    print('#{} {}'.format(tc, cnt))