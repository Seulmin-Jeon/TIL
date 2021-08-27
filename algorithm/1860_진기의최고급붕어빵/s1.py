import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    # N: 자격을 얻은 사람
    # M: K개의 붕어빵을 만드는 데에 걸리는 시간
    N, M, K = map(int, input().split())

    # 각 손님이 언제 도착하는지 (N명)
    guest = list(map(int, input().split()))
    guest.sort()     # 먼저 오는 손님 순으로 정렬!

    result = 'Possible'
    # for i in guest:
    #     if i < M:
    #         result = 'Impossible'

    for p in range(N):
        b = (guest[p]//M) * K
        if b < p+1:
            result = 'Impossible'
            break

    print('#{} {}'.format(tc, result))