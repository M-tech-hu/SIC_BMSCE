n = int(input())

a = []
temp = input().split()

for i in range(n):
    a.append(int(temp[i]))

temp = input().split()
q = int(temp[0])
x = int(temp[1])

stack = []
s = 0
k = 0

for i in range(q):
    op = input()

    if op == "Harry":
        stack.append(a[k])
        s = s + a[k]
        k = k + 1

    else:
        s = s - stack.pop()

    if s == x:
        print(len(stack))
        break
    