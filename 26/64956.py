"""

"""
# [[время_прихода, необходимое_время, вид_услуги]...]
data = [list(map(int, line.split())) for line in open('64956.txt').readlines()[1:]]
data.sort()

# Время в которое окно освободится
windows = [0] * 10
lefts = 0
for start_time, need_time, window in data:
    if start_time + 30 >= windows[window]:
        # Может ждать
        windows[window] = need_time + (start_time if windows[window] < start_time else windows[window])
    else:
        # Не может ждать
        lefts += 1
print(lefts)