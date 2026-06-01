n, x = input().split()
n = int(n)
x = int(x)

temp = input().split()
coins = []

for i in range(n):
    coins.append(int(temp[i]))

m = int(input())

stack = []
total = 0
index = 0
answer = -1

for i in range(m):
    op = input()

    if op == "Harry":
        stack.append(coins[index])
        total += coins[index]
        index += 1

    elif op == "Remove":
        if len(stack) > 0:
            total -= stack.pop()

    if total == x:
        answer = len(stack)
        break

print(answer)