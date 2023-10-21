def f(n):
    a = ''
    while n > 0:
        a = str(n % 3) + a
        n //= 3
    return a


m = 10000
for n in range(1, 1000):
    a = f(n)
    if n % 3 == 0:
        a += a[-3:]
    else:
        a += f(n % 3 * 3)
    r = int(a, 3)
    if r > 150:
        m = min(n, m)
print(m)
