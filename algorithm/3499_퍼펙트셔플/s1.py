import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    Deque = input().split()

    if len(Deque) % 2:
        group1 = Deque[:len(Deque)//2+1]
        group2 = Deque[len(Deque)//2+1:]
    else:
        group1 = Deque[:len(Deque)//2]
        group2 = Deque[len(Deque)//2:]

    result = []
    while len(group1) > 0:
        a = group1.pop(0)
        result.append(a)
        if len(group2) > 0:
            b = group2.pop(0)
            result.append(b)

    ans = ' '.join(result)
    print('#{} {}'.format(tc,ans))