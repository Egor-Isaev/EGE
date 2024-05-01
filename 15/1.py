def d(n, m):
    if n % m == 0:
        return True
    if n % m != 0:
        return False


for a in range(64):
    f = True
    for x in range(64):
        if not (not (d(x, a)) <= (d(x, 28) <= not (d(x, 49)))):
            f = False
    if f:
        print(a)
