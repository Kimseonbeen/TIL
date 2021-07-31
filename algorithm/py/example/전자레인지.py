n = int(input())

arr = [300, 60, 10]
arrN = [0, 0, 0]

for i in range(len(arr)):
    arrN[i] += n // arr[i]
    n %= arr[i]
if n != 0:
    print(-1)
else:
    print(' '.join(str(e) for e in arrN))
    
