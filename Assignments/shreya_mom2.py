n, p = input().split()
n = int(n)
p = int(p)

a = []
for x in input().split():
    a.append(int(x))

a.sort()

money = 0

for i in range(p):
    if i < n and a[i] < 0:
        money += -a[i]

print(money)