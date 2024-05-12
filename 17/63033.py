s = list(map(int, open('63033.txt').readlines()))
cnt = 0
maxx = 0
a = [x for x in s if x % 1000 == 123]
for i in range(1, len(s) - 2):
    p = sum([int(9999 < s[i] < 100000), int(9999 < s[i + 1] < 100000), int(9999 < s[i + 2] < 100000)])
    q = sum([int(s[i] % 3 == 0), int(s[i + 1] % 3 == 0), int(s[i + 2] % 3 == 0)])
    if p >= 2 and q == 1 and s[i] + s[i + 1] + s[i + 2] > max(a):
        cnt += 1
        maxx = max(maxx, s[i] + s[i + 1] + s[i + 2])
print(cnt, maxx)
