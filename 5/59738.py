m = 0
for n in range(1, 10000):
    a = bin(n)[2:]
    if n % 3 == 0:
        a1 = a + a[-3:]
    else:
        b = n % 3
        b1 = bin(b * 3)[2:]
        a1 = a + b1
    r = int(a1, 2)
    if r <= 137:
        m = max(m, r)
print(m)
