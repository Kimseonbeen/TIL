# 구현
## 구현이란, 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정

# 흔히 알고리즘 대회에서 구현 유형의 문제란 무엇을 의미할까요?
## 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
# 구현 유형의 예시는 다음과 같습니다
## 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
## 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
## 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
## 적절한 라이브러리를 찾아서 사용해야 하는 문제 

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x,y = 2,2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

# <문제> 상하좌우

# N 입력 받기
## n = int(input())
n = 5
x, y = 1,1
## plans = input().split()
plans = ['R', 'R', 'R', 'U', 'U']
print(plans)
# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U','D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    print("plan : ",plan)
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)


# <문제> 시각
## 완전 탐색 문제
# h = int(input())
h = 5
count = 0

for i in range(h + 1):  # 인덱스 0부터 시작하므로 h + 1 해준다
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k): ## 반복문 돌때마다 시 분 초 문자열을 더해 3이 포함되어있는지 확인
                count += 1
print(count)

# <문제> 왕실의 나이트
## 요구사항대로 충실히 구현하면 되는 문제
## 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인합니다.
## 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의합니다.

# 현재 나이트의 위치 입력받기
# input_data = input()
input_data = "a1"
row = int(input_data[1])
print("row : ",row)
column = int(ord(input_data[0])) - int(ord('a')) + 1    # 아스키 코드 치환
print("column : ",column)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)

# <문제> 문자열 재정렬
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))