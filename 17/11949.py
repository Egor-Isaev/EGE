a = list(map(int, open('11949.txt').readlines()))
cnt = 0
m = 0
b = [x for x in a if abs(x) % 100 == 68]
maxx = max(b)
for i in range(0, len(a) - 3):
    c = sum([int(9<abs(a[i])<100),int(9<abs(a[i+1])<100),int(9<abs(a[i+2])<100),int(9<abs(a[i+3])<100)])
    if (c==1 or c==4) and (a[i] + a[i + 1] + a[i + 2] + a[i + 3] >= maxx):
        cnt += 1
        m = max(m, a[i] + a[i+1] + a[i + 2] + a[i + 3])
print(cnt, m)
