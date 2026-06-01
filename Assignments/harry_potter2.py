n = int(input())

temp = input().split()
coins = []

for i in range(n):
    coins.append(int(temp[i]))

temp = input().split()
q = int(temp[0])
x = int(temp[1])

stack = []
sum = 0
index = 0

for i in range(q):
    op = input()

    if op == "Harry":
        stack.append(coins[index])
        sum += coins[index]
        index += 1

    else:  # Remove
        sum -= stack.pop()

    if sum == x:
        print(len(stack))
        break