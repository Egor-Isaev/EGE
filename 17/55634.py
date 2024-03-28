a = list(map(int, open('55634.txt').readlines()))
m = 10000
c = 0
para = 0
for g in range(0, len(a)):
    if abs(a[g]) % 10 == (abs(a[g]) % 100) // 10 and a[g] < m:
        m = a[g]
for i in range(0, len(a) - 1):
    if (a[i] ** 2 + a[i + 1] ** 2 < m ** 2) and (
            (abs(a[i]) % 13 == 0 and abs(a[i + 1]) % 13 != 0) or (abs(a[i]) % 13 != 0 and abs(a[i + 1]) % 13 == 0)) and (
            (abs(a[i]) % 10 == abs(a[i + 1]) % 100 // 10) or (abs(a[i+1]) % 10 == abs(a[i]) % 100 // 10)):
        c += 1
        para = max(para, a[i]**2 + a[i+1]**2)
print(c,para)
