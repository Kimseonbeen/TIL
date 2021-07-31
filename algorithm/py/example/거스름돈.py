n = 1260
count = 0

money = [500, 100, 50, 10]

for i in money:
    count += n // i
    print("n1 :", n)
    print("i :", i)
    n = n % i
    print("n2 :", n)
print(count)