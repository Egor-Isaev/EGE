m=10000
for n in range(1, 1000):
    a = bin(n)[2:]
    if n % 3 == 0:
        a1 = a + a[-3:]
    else:
        v = n % 3
        b = bin(v * 3)[2:]
        a1 = a + b
    r = int(a1, 2)
    if r > 151:
        m = min(r,m)
print(m)
