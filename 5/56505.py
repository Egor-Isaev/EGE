def f(n):
    if n < 10:
        return n
    else:
        return n % 10 + f(n // 10)

cnt = 0
for n in range(17, 10000):
    b = bin(n)[2:]
    if f(n) % 2 != 0:
        b1 = b + '1'
    else:
        b1 = b + '0'
    n1 = int(b1, 2)
    if f(n1) % 2 != 0:
        b2 = b1 + '1'
    else:
        b2 = b1 + '0'
    n2 = int(b2, 2)
    if f(n2) % 2 != 0:
        b3 = b2 + '1'
    else:
        b3 = b2 + '0'
    r = int(b3, 2)
    if r/n == 8:
        cnt += 1
    print(cnt)