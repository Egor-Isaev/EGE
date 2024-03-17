line = open('36037.txt').readline()
lens = list(map(len, line.replace('XZZY','XZZYXZZY').split('XZZY')))
max_len = 0
for i in range(len(lens)):
    total_len = lens[i]
    if i > 0 and lens[i - 1] == 0:
        total_len += 3
    if i < len(lens) - 1 and lens[i + 1] == 0:
        total_len += 3
    max_len = max(max_len, total_len)
print(max_len)
# 1713