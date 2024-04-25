a = list(map(int, open('сг3.txt').readlines()))
s = [x for x in a if x % 1000 == 652]
k = 2 * (max(s) + min(s))
cnt = 0
maxx = 0
for i in range(1, len(a) - 3):
    d = sum([int(9999 < a[i] < 100000), int(9999 < a[i + 1] < 100000), int(9999 < a[i + 2] < 100000),
             int(9999 < a[i + 3] < 100000)])
    h = sum([int(999 < a[i] < 10000), int(999 < a[i + 1] < 10000), int(999 < a[i + 2] < 10000),
             int(999 < a[i + 3] < 10000)])
    g = sum([int(a[i] % 3 == 0), int(a[i + 1] % 3 == 0), int(a[i + 2] % 3 == 0), int(a[i + 3] % 3 == 0)])
    p = sum([int(a[i] % 7 == 0), int(a[i + 1] % 7 == 0), int(a[i + 2] % 7 == 0), int(a[i + 3] % 7 == 0)])
    if d > h and g == p and a[i]+a[i+1]+a[i+2]+a[i+3] > k:
        cnt += 1
        maxx = max(maxx, a[i]+a[i+1]+a[i+2]+a[i+3])
print(cnt, maxx)


