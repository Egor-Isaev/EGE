s = list(map(int, open('сг2.txt').readlines()))
c = 0
maxx = 0
m = 0
b = [x for x in s if abs(x) % 1000 == 123]
maxx = max(b)
for i in range(0, len(s) - 2):
    d = sum([int(9999 < s[i] < 100000), int(9999 < s[i + 1] < 100000), int(9999 < s[i + 2] < 100000)])
    h = sum([int(s[i] % 3 == 0), int(s[i + 1] % 3 == 0), int(s[i + 2] % 3 == 0)])
    if (d==2 or d==3) and h == 1 and s[i]+s[i+1]+s[i+2]>maxx:
        c += 1
        m = max(m,s[i]+s[i+1]+s[i+2])
print(c,m)