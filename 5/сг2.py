m = [0] * 1000000
maxx = 0
for n in range(1, 1000):
    d = bin(n)[2:]
    g = bin(n % 4)[2:]
    r = int((d + g), 2)
    m[r] = 1
for i in range(1000000 - 49):
    maxx = max(maxx, sum(m[i:i + 49]))
print(maxx)
