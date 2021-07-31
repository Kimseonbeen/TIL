n = int(input())

money = 1000 - n

jandon = [500, 100, 50, 10, 5, 1]

count = 0

print(money)

for i in jandon:
    count += money // i
    money %= i
    print(money)

print(count)
