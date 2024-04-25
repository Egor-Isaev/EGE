s = list(map(int, open('дос17.txt').readlines()))
cnt = 0
maxx = 0
a = [x for x in s if x % 19 == 0]
for i in range(0, len(s) - 1):
    if (s[i] > max(a) and s[i + 1] > max(a)) or (s[i] > max(a) and s[i + 1] < max(a)) or (
            s[i] < max(a) and s[i + 1] > max(a)):
        cnt += 1
        maxx = max(maxx,s[i]+s[i+1])
print(cnt,maxx)