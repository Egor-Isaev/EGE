l = []
for a_min in range(1, 100):
    for a_max in range(1, 100):
        f = True
        for x in range(1,100):
            if not ((x in range(23, 59) or (x in range(a_min, a_max))) <= ((
                    x in range(1, 40) or (x in range(a_min, a_max))))):
                f = False
        if f:
            l.append(a_max - a_min)
print(min(l))
