n = int(input())
count = 0
b = [5,3]

for i in b:
    count += n // i
    print("count :",count)
    print("i :", i)
    n = n % i
    print(n)

print(count)