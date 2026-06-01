n, p = input().split()
n = int(n)
p = int(p)

prices = []
for x in input().split():
    prices.append(int(x))

prices.sort()

money = 0
count = 0

for i in range(n):
    if prices[i] < 0 and count < p:
        money += -prices[i]
        count += 1
    else:
        break

print(money)