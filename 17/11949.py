s = list(map(int, open('11949.txt').readlines()))
cnt = 0
maxx = 0
l = [x for x in s if x % 100 == 68]
for i in range(0, len(s) - 3):
    p = sum([int(9 < abs(s[i]) < 100), int(9 < abs(s[i + 1]) < 100), int(9 < abs(s[i + 2]) < 100),
             int(9 < abs(s[i + 3]) < 100)])
    if (p == 1 or p == 4) and s[i]+s[i+1]+s[i+2]+s[i+3] >= max(l):
        cnt += 1
        maxx = max(maxx,s[i]+s[i+1]+s[i+2]+s[i+3])
print(cnt,maxx)
