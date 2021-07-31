n = list(map(int, input().split()))

N = n[0]
K = n[1]
count = 0
coin = []

for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

print(coin)

for i in coin:
    count += K // i
    K %= i

print(count)