# 그리디 알고리즘
## 그리디 알고리즘(탐욕법)은 !현재 상황에서 지금 당장 좋은 것만 고르는 방법!
## 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
## 그리디 해법은 그 정당성 분석이 중요
### 단순히 가장 좋아 보이는 것을 반복적으르 선택해도 !최적의 해!를 구할 수 있는지 검토

## 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많습니다.
## 하지만 코딩테스트에서의 대부분의 그리디 문제는 !탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론!할 수 있어야 풀리도록 출제됩니다.

# <문제> 거스름 돈
# 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는?
## 가지고 있는 동전 중에서 !큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 떄문!
## ex. 만약 800원을 거슬러 주는 문제일시 화폐 단위가 500원, 400원, 100원이라면
## 탐욕법에 의해 500원 1개, 100원 3개가 아니라 400원 2개가 정답
### 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 한다.

# <문제> 거스름 돈 : 답안 예시
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
print(count)

# <문제> 거스름 돈 : 시간 복잡도 분석
## 화폐의 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K)입니다.
## 이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받습니다.

# <문제> 1이 될 때까지: 문제 해결 아이디어
## 주어진 N에 대하여 최대한 많이 나누기를 수행하면 됩니다.
## N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있습니다.

# n, k = map(int, input().split())
n = 25
k = 5
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    print("target : ",target)
    result += (n - target)
    print("result1 : ", result)
    n = target
    print("n : ", n)
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
    print("n2 : ", n)
    print("result2 : ", result)

print("result ! : ", result)
# 마지막으로 남은 수에 대하여 1씩 빼기
result -= 1
print(result)

# <문제> 곱하기 혹은 더하기

# data = input()
data = "57774"
# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
print("result data  :",result)

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    print("num + ",num)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# 모험가 길드
n = int(input())
data = list(map(int, input().split()))
data.sort()
print("data : ", data)

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    print("i : ", i)
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        print("result : ",result)
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result) # 총 그룹의 수 출력
