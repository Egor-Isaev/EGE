l = open('дос.txt').readline()
maxx = 0
cnt = 1
l = l.replace('A', '@')
l = l.replace('B', '@')
l = l.replace('C', '@')
l = l.replace('6', '*')
l = l.replace('7', '*')
l = l.replace('8', '*')
l = l.replace('9', '*')
for i in range(1, len(l)):
    if l[i - 1] + l[i] != '@@' and l[i - 1] + l[i] != '**':
        cnt += 1
        maxx = max(maxx, cnt)
    else:
        cnt = 1
print(maxx)
