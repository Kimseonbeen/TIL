# n, k = map(int, input().split())
n = 17
k = 4
count = 0
while True:
    if n // k != 1:
        print("a ")
        target = n - ((n // k) * k)
        count += target
        print("count : ",target)
        n = (n // k) * k
        print("n : ",n)
    print("count : ", target)
    if n < k:
        break
    n //= k
    count += 1
    print("aaa")

print(count)