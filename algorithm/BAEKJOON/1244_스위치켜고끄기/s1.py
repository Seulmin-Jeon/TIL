import sys
sys.stdin = open('input.txt')

'''
남학생: 받은 수의 배수 번호의 스위치 상태를 바꿈
여학생: 받은 수의 양쪽 대칭으로 개수가 같으면서 최대인 범위의 스위치 상태를 모두 바꿈
(대칭인 범위가 없으면 받은 번호의 스위치 상태만 바꿈)
'''


N = int(input())   # 스위치의 개수
state = [9] + list(map(int, input().split()))   # 스위치의 상태 (off 0 / on 1)
n = int(input())   # 학생수
student = [list(map(int, input().split())) for _ in range(n)]   # 학생의 성별(남1 여2), 받은 번호

for i in range(n):
    # 남학생인 경우
    if student[i][0] == 1:
        a = student[i][1]   # 남학생이 받은 번호
        for k in range(a, N+1, a):
            if state[k] == 0:
                state[k] = 1
            elif state[k] == 1:
                state[k] = 0
    # 여학생인 경우
    else:
        b = student[i][1]   # 여학생이 받은 번호

        i = 0   # i=0인 경우는 받은 번호 자기 자신과 비교 (무조건 바뀜)
        while 0 <= b-i <= N and 0 <= b+i <= N:
            if state[b-i] == state[b+i]:
                if state[b-i] == 0:
                    state[b-i] = 1
                    state[b+i] = 1
                elif state[b-i] == 1:
                    state[b-i] = 0
                    state[b+i] = 0
                i += 1
            else:
                break

for i in range(1, N+1):
    print(state[i], end = ' ')
    if i % 20 == 0:
        print()