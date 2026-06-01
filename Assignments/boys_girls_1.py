t = int(input())

for _ in range(t):
    n = int(input())

    boys = []
    girls = []

    temp = input().split()
    for i in range(n):
        boys.append(int(temp[i]))

    temp = input().split()
    for i in range(n):
        girls.append(int(temp[i]))

    boys.sort()
    girls.sort()

    boys_first = True
    girls_first = True

    for i in range(n):
        if boys[i] >= girls[i]:
            boys_first = False

        if girls[i] >= boys[i]:
            girls_first = False

    if boys_first or girls_first:
        print("YES")
    else:
        print("NO")