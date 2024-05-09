s = list(map(int, open('61397.txt').readlines()))
cnt = 0
maxx = 0
a = [x for x in s if x % 100 == 17]
for i in range(1, len(s) - 2):
    c = sum([int(999 < s[i] < 10000), int(999 < s[i + 1] < 10000), int(999 < s[i + 2] < 10000)])
    d = sum([int(s[i] % 5 == 0), int(s[i + 1] % 5 == 0), int(s[i + 2] % 5 == 0)])
    if c == 2 and d >= 1 and s[i] + s[i+1] + s[i+2] > max(a):
        cnt += 1
        maxx = max(maxx,s[i] + s[i+1] + s[i+2])
print(cnt, maxx)
