t = int(input())

for i in range(t):
    n = int(input())

    boys = [int(x) for x in input().split()]
    girls = [int(x) for x in input().split()]

    boys.sort()
    girls.sort()

    c1 = True
    c2 = True

    for j in range(n):
        if boys[j] >= girls[j]:
            c1 = False

        if girls[j] >= boys[j]:
            c2 = False

    if c1 or c2:
        print("YES")
    else:
        print("NO")