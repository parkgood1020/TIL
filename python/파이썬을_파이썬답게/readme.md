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

## 5. 정렬된 리스트 구하기
파이썬에서 원본을 유지한채 정렬된 리스트를 구하고자 할때는 `sorted`를 사용하면 된다. <br>
```
list1 = [3, 2, 1]
list2 = sorted(list1)  #list2 = [1,2,3]
```
## 6. zip 함수
`zip(*iterables)`는 각 iterables의 요소들을 모으는 이터레이터를 만든다. <br>
```
mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)
```

## 7. map 함수
파이썬에서는 map 함수를 사용하면 for문을 사용하지 않고도 멤버의 타입을 일괄 변환할 수 있다.
```
# 1. for문
list1 = ['1', '100', '33']
list2 = []
for value in list1:
    list2.append(int(value)) #list2 = [1,100,33]
    
# 2. map함수    
list1 = ['1', '100', '33']
list2 = list(map(int, list1) #list2 = [1,100,33]   
```

## 8. 곱집합 구하기.
```
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)
```
위 코드를 파이썬에서는 `itertools.product`를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있다.
```
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
```

## 9. join 함수
```
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value  #answer = 110033
```
파이썬의 str.join(iterable)을 사용하면 이 코드를 두 줄로 줄일 수 있다.
```
my_list = ['1', '100', '33']
answer = ''.join(my_list)
```

