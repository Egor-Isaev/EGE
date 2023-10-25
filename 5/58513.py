m = 0
for n in range(1, 1000000):
    a = bin(n)[2:]
    if n % 5 == 0:
        a += bin(5)[2:]
    else:
        a += '1'
    if int(a, 2) % 7 == 0:
        a += bin(7)[2:]
    else:
        a += '1'
    r = int(a, 2)
    if r < 1855663:
        m = max(m, n)
print(m)
