s = open('59849.txt').readline()
g = '0123456789ABCDEFGHIJKLMNOP'
cnt = 0
maxx = 0
for i in range(1, len(s)):
    if s[i] in g:
        cnt += 1
    else:
        cnt = 0
    maxx = max(maxx, cnt)
print(maxx)
