def f(n):
    a = ''
    if n < 3:
        return n
    else:
        while n > 0:
            a += str(n % 3)
            n = n // 3
        return a[::-1]

minn = 100000
for n in range(1, 1000):
    b = str(f(n))
    if n % 3 == 0:
        b = b + b[-3:]
    else:
        b = b + str(f((n % 3) * 3))
    r = int(b, 3)
    if r > 150:
        minn = min(n, minn)
print(minn)
