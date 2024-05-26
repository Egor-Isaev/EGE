a = open('24_16388.txt').readlines()
cnt = 0
for i in range(1, len(a)):
    if a[i] == 'K' and a[i + 1] == 'L' and a[i + 2] == 'M' and a[i + 3] == 'N':
        cnt += 1
print(cnt)