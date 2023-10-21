def f(n):
    a = ''

    while n > 0:
        a = str(n % 3) + a
        n //= 3
    return a


for n in range(1, 10000):
    w = f(n)
    if n % 3 != 0:
        w += f(n % 3 * 5)
    r = int(w, 3)
    if r > 146:
        print(n)
        break
