
cnt = 0
for a in range(1,10000):
    d = oct(a) [2:]
    s = []
    s = s.append(d)
    for i in s:
        g = bin(a) [2:]
        if len(d) == 16 and s[i] + s[i+1] % 2 != 0 and g.count('111') == 0:
            cnt += 1