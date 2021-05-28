# 파이썬을 파이썬답게 학습 내용 정리
이 페이지는 `프로그래머스 - 파이썬을 파이썬답게` 강의를 수강하고 정리한 내용입니다.<br>
(출처 - https://programmers.co.kr/learn/courses/4008)

## 1. divmod
파이썬의 `divmod`와 `unpacking`을 이용하면 다음과 같이 몫과 나머지를 한번에 구할 수 있다.
```
a = 7
b = 5
print(*divmod(a, b)) => 1, 2
```

## 2. 진법 변환
파이썬의 `int` 함수는 진법 변환을 지원한다. 사용 방법은 아래와 같다.
```
num = '3212'
base = 5
answer = int(num, base)  # 432
```
## 3. 문자열 정리
파이썬에서는 `ljust`, `center`, `rjust`와 같은 `string`의 메소드를 사용해 코드를 줄일 수 있다.
```
s = '가나다라'
n = 7

s.ljust(n)    # 좌측 정렬
s.center(n)   # 가운데 정렬
s.rjust(n)    # 우측 정렬

'가나다라               ' # 좌측정렬
'               가나다라' # 우측 정렬
'       가나다라        ' # 가운데 정렬
```

## 4. 알파벳 출력하기

파이썬은 아래의 데이터를 상수로 정리하였다.
```
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```

