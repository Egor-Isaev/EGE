def d(n, m):
    return n % m == 0


for a in range(1, 3000):
    f = True
    for x in range(1, 3000):
        if not ((not d(x, a)) <= (d(x, 28) <= (not d(x, 49)))):
            f = False
    if f:
        print(a)
