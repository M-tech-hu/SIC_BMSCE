n = int(input())

arr = []
for x in input().split():
    arr.append(int(x))

pivot = arr[n - 1]
k = 0

for i in range(n - 1):
    if arr[i] <= pivot:
        arr[i], arr[k] = arr[k], arr[i]
        k += 1

arr[k], arr[n - 1] = arr[n - 1], arr[k]

for i in range(n):
    print(arr[i], end=" ")