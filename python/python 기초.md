# python 기초



### 1. 이스케이프 시퀀스 (\\\)

```
\n 줄바꿈
\t 탭
\\ \
\' '
\" "
```



### 2. String interpolation

```
f-strings
출력형식 지정, 연산 가능

ex.
name = 'seulmin'
print(f'안녕하세요, {name}')
```



### 3. 형변환

```
암시적 형변환
print(True + 100)
101
```

```
명시적 형변환
```



### 4. 연산자

```
산술 연산자
// 몫
% 나머지
** 거듭제곱

print(divmod(5, 2))
(2, 1) = (몫, 나머지)
```

```
비교 연산자
== 같음
!= 같지 않음
```

```
논리 연산자
and, or, not
* 단축평가
결과가 확실한 경우 두번째 값 확인하지 않고 첫번째 값 반환
```

```
복합 연산자
+=, *= ...

ex.
cnt = 0
while cnt < 5:
    print(cnt)
    cnt += 1
```



### 5. Concatenation

: + 연산자로 결합



### 6. Containment Test

```python
'a' in 'apple'
1 in [1, 2, 3]
```







```python
# 문제) 계단 만들기
number = int(input())

for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end='')
    print()
```



