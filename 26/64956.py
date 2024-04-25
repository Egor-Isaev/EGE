"""

"""
# [[время_прихода, необходимое_время, вид_услуги]...]
data = [list(map(int, line.split())) for line in open('64956.txt').readlines()[1:]]
data.sort()

# Время в которое окно освободится
windows = {item[2]: [0, 0] for item in data}
lefts = 0
for start_time, need_time, window in data:
    if start_time + 30 >= windows[window][0]:
        # Может ждать
        windows[window][0] = need_time + (start_time if windows[window][0] < start_time else windows[window][0])
        windows[window][1] += 1
    else:
        # Не может ждать
        lefts += 1

print(lefts)
print(windows)
