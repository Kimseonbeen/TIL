# 자료형
# 파이썬의 자료형으로는 정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전 등이 있다.

# 정수형(Integer)은 정수를 다루는 자료형
# 양의 정수, 음의 정수, 0 포함

# 양의 정수
a = 1000
print(a)    # 1000

# 음의 정수
a = -7
print(a)    # -7

# 0
a = 0
print(a)    # 0

# 실수형(Real Number)은 소수점 아래의 데이터를 포함하는 수 자료형
# 파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리
# 소수부가 0 이거나, 정수부가 0인 소수는 0을 생략하고 작성할 수 있다.

# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 지수 표현 방식
# 파이썬에서는 e, E를 사용한 지수 표현 방식을 이용할 수 있다.
# e나 E 다음에 오는 수는 10의 지수부를 의미
# 예를 들어 1e9라고 입력하게 되면, 10의 9제곱(1,000,000,000)이 된다. 1 x 10의 9제곱

# 10억
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

# 실수형 더 알아보기
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else :
    print(False)    # 컴퓨터는 2진수 체계라 정확하게 표현할 수 없다.

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)    # round 함수를 사용


a = 7
b = 3

# 나누기
print(a / b)    # py는 나누기 연산자 사용시 몫만 나오는게 아니라 그 뒤에 실수까지 표시

# 나머지
print(a % b)

# 몫
print(a // b)

# 리스트 자료형
# 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
# Array 기능 및 연결 리스트와 유사한 기능
# 리스트 대신에 배열 혹은 테이블이라고 부르기도 한다

# 직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 네 번째 원소만 출력
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 인데스 값을 입력하여 리스트의 특정한 원소에 접근하는 것을 인덱싱이라고 한다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 여덟 번째 원소만 출력
print(a[7])

# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = 7
print(a)

# 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱을 이용한다.
# 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수 있다.
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정해야한다.

# 두 번째 원소부터 네 번째 원소까지
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1 : 4])

# 리스트 컴프리헨션
a = [ i for i in range(50)]
print(a)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# 리스트 컴프리헨션과 일반적인 코드 비교하기

# 코드 1 : 리스트 컴프리헨션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 코드 2 : 일반적인 코드
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# 리스트 컴프리헨션 (잘못된 예시)
# N X M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 4
n = 3
array = [[0] * m] * n   # 모두 같은 객체로 인식하여 수정시 다 바뀜
print(array)

array[1][1] = 5
print(array)

# 언더바는 언제 사용하나요 ?
# 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때 언더바(_)를 자주 사용합니다.

# 코드 1 : 1부터 9까지의 자연수 더하기
summary = 0
for i in range(1, 10):
    summary += i
print(summary)

# 코드 2 : "Hello World"를 5번 출력하기
for _ in range(5):
    print("Hello World")

# 리스트 관련 기타 메서드

a = [1, 4, 3]
print("기본 리스트 : ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입 : ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬 : ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬 : ", a)

a = [4, 3, 2, 1]

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기 : ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가 : ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제 : ", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_list에 포함되지 않는 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

# 문자열 자료형

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2 : 4])

# 튜플 자료형
# 튜플 자료형은 리스트와 유사한지만 다음과 같은 문법적 차이가 있습니다.
# 튜플은 한 번 선언된 값을 변경할 수 없습니다.
# 리스트는 대괄호[]를 이용하지만, 튜플은 소괄호()를 이용합니다.
# 튜플은 리스트에 비해 상대적으로 공간 효율적입니다.
print("튜플 자료형--------------")
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 네 번째 원소만 출력
print(a[3])

# 두 번째 원소부터 네 번째 원소까지
print(a[1 : 4])

# a = (1, 2, 3, 4) 변경 불가능이라 오류남

### 튜플을 사용하면 좋은 이유
## 서로 다른 성질의 데이터를 하나로 묶어서 관리해야 할 때
# 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용합니다.

## 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
# 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있습니다.

## 리스트 보다 메모리를 효율적으로 사용해야 할 때

### 사전 자료형
## 사전 자료형은 키(key)와 값(Value)의 쌍을 데이터로 가지는 자료형입니다.
# 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됩니다.

## 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 변경 불가능한 자료형을 키로 사용 할 수있습니다.

## 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.
print("사전 자료형 ---")
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Cocount'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

### 사전 자료형 관련 메서드
## 사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원합니다.
# 키 데이터만 뽑아서 리스트로 이용할 때는 keys()함수를 이용합니다.
# 값 데이터만을 뽑아서 리스트로 이용할 때는 Values()함수를 이용합니다. 

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 이런식으로도 사전 자료형 선언 가능
b = {
    '홍길동' : 97,
    '이순신' : 98
}
print(b)
key_list = list(b.keys())   # 리스트로 형변환하여 출력
print(key_list)

### 집합 자료형
## 집합은 다음과 같은 특징이 있습니다.
# 중복을 허용하지 않습니다.
# 순서가 없습니다.

## 집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있습니다.
# 이때 set()함수를 이용합니다.

## 혹은 중괄호{}안에 각 원소를 콤마(,)를 기준으로 구분하여 삽입함으로써 초기화 할 수 있습니다.
## 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.
print("집합 자료형 ----")

# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

## 기본적인 집합 연산으로는 합집합, 교집합, 차집합 연산 등이 있습니다.
# 합집합 : 집합 A에 속하거나 B에 속하는 원소로 이루어진 집합 (A U B)
# 교집합 : 집합 A에도 속하고 B에도 속하는 원소로 이루어진 집합 (A N B)
# 차집합 : 집합 A의 원소 중에서 B에 속하지 않는 원소들로 이루어진 집합 (A - B)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print("합집합 :",a | b)

# 교집합
print("교집합 :",a & b)

# 차집합
print("차집합 :",a - b)

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print("집합 자료형 관련 함수 : ",data)

# 새로운 원소 추가
data.add(4)
print("새로운 원소 추가 : ",data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print("새로운 원소 여러 개 추가 : ",data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print("특정한 값을 갖는 원소 삭제 : ",data)

## 사전 자료형과 집합 자료형의 특징
## 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있습니다.

## 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
# 사전의 키(Key)혹은 집합의 원소(Element)를 이용해 O(1)의 시간 복잡도로 조회합니다. 

### 기본 입출력
## 모든 프로그램은 적절한 (약속된) 입출력 양식을 가지고 있습니다.
## 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것입니다.
## 예시) 학생의 성적 데이터가 주어지고, 이를 내림차순으로 정렬한 결과를 출력하는 프로그램

### 자주 사용되는 표준 입력 방법
## input() 함수는 한 줄의 문자열을 입력 받는 함수입니다.

## map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용합니다.
# 예시) 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용합니다.
# list(map(int, input().split()))
# 예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용합니다.
# a, b, c = map(int, input().split)

### 입력을 위한 전형적인 소스코드 1)

# # 데이터의 개수 입력
# n = int(input())
# # 각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))  # 입력받은 데이터를 모두 map 함수로 정수형 형변환 시켜준다

# data.sort(reverse=True)
# print(data)

### 입력을 위한 전형적인 소스코드 2)
# n, m, k = map(int, input().split())
# print(n, m, k)

### 빠르게 입력 받기

## 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있습니다.

## 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용합니다.
# 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드로 함께 사용합니다.

# 속도 향상 문자열 입력 받기
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

### 자주 사용되는 표준 출력 방법
## 파이썬에서는 기본 출력은 print() 함수를 이용합니다.
# 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할 수 있습니다.

## print()는 기본적으로 출력 이후에 줄 바꿈을 수행합니다.
# 줄 바꿈을 원치 않는 경우 'end' 속성을 이용 할 수 있습니다.

print("출력을 위한 전형적인 소스코드")

# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

# 출력할 변수
answer = 7
print(" 정답은 " + str(answer) + "입니다.")

### f-string 예제
## 파이썬 3.6부터 사용 가능하며, 문자열 앞에 접두사 'f'를 붙여 사용합니다.
## 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있습니다.
answer = 7
print(f"정답은 {answer}입니다.")

# 조건문 예제
x = 15
if x >= 10:
    print("x >= 10")
if x >= 0:
    print("x >= 0")
if x >= 30:
    print("x >= 30")

score = 85

if score >= 70:
    print("성적이 70점 이상입니다.")
    if score >= 90:
        print("우수한 성적입니다.")
else:
    print("성적이 70점 미만입니다.");
    print("조금더 분발하세요.")

print("프로그램을 종료합니다.")

a = 5

if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >= -10")
else:
    print("-10 > a")

# 파이썬의 pass 키워드
## 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용합니다.

score = 85

if score >= 80:
    pass # 나중에 작성할 코드입니다.
else:
    print('성적이 80점 미만입니다.')
print("프로그램을 종료합니다.")

# 조건문의 간소화

score = 85

if score >= 80: result = "Success"
else: result = "Fail"
print(result)

# 1부터 9까지 모든 정수의 합 구하기 예제(while문)

i = 0
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
    #print(i)
print(result)

# 반복문: for문
## 반복문으로 for문을 이용할 수도 있습니다.
## for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 'in' 뒤에 오는 데이터(리스트, 튜플 등)에 포함
## 되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문합니다.

# for 변수 in 리스트:
#   실행할 소스코드

array = [9,8,7,6,5]

for x in array:
    print(x)


# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용합니다.
## 이때 range(시작 값, 끝 값 +1) 형태로 사용합니다.
## 인자를 하나만 넣으면 자동으로 시작 값은 0이 됩니다.

result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i
print(result)

# 함수 정의하기

# def 함수명(매개변수):
#    #실행할코드
#    return 반환값

a = 10
# 함수안에서 전역변수 사용하고 싶을 시 global를 사용한다
def func():
    global a
    a += 1
    print(a)

func()

# 여러 개의 반환 값
# 패킹
def operator(a,b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    return add_var, subtract_var, multiply_var
# 언패킹
a,b,c = operator(7,3)
print(a,b,c)

# 람다 표현식
print((lambda a,b: a + b)(3,6))

# 람다 표현식 예시
array = [('홍길동',50), ('이순신',32), ('아무개',75)]
 
# 정렬기준 명시 두번째 값
def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# 람다 표현식 예시: 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))

# 자주 사용되는 내장 함수
## sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 순열과 조합
## 모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 효과적으로 사용할 수 있을까요?
## 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
## {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우 : 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
## 조합 : 서로 다른 n개에서 !순서에 상관없이! 서로 다른 r개를 선택하는 것
## {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우 : 'AB', 'AC', 'BC'

# 순열
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data,3)) # 모든 순열 구하기
print(result)

# 조합
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data,2)) # 2개를 뽑는 모든 조합 구하기
print(result)

# 중복 순열
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# 증복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

# Counter
## 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공합니다.
## 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려줍니다.

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'blue'가 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

# 최대 공약수와 최소 공배수
## 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수를 이용할 수 있습니다.

import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
    return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14)) # 최소 공배수(LCM) 계산