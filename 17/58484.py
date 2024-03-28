a = list(map(int, open('58484.txt').readlines()))
cnt = 0
u = 20001
maxx = 0
for i in range(len(a)):
    if str(a[i])[-1] == '5':
        if len(str(a[i])) == 3:
            u = min(a[i], u)
for i in range(len(a) - 1):
    if (999 < a[i] < 10000 and not (999 < a[i + 1] < 10000)) or (999 < a[i + 1] < 10000 and not (999 < a[i] < 10000)):
        if (a[i] ** 2 + a[i + 1] ** 2) % u == 0:
            cnt += 1
            maxx = max(maxx, a[i] ** 2 + a[i + 1] ** 2)
print(cnt, maxx)
