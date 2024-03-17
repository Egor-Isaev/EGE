a = list(map(int, open('39763.txt').readlines()))
count = 0
m = 0
for i in range(1, len(a) - 2):
    sides = sorted([a[i],a[i+1],a[i+2]])
    if sides[0]**2 + sides[1]**2 > sides[2]**2:
        count += 1
        m = max(m,a[i]+a[i+1]+a[i+2])

print(count,m)
