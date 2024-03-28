m = 10000
for n in range(1,1000):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b + '00'
    else:
        b = b + '11'
    r = int(b,2)
    if r > 114:
        m = min(r,m)
print(m)