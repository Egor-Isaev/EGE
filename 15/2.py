l = []
for a_min in range(-200, 200):
    for a_max in range(-200, 200):
        f = True
        for x in range(200):
            if not ((x in range(47, 115+1)) <= (((not (x in range(a_min, a_max + 1))) and (x in range(24, 90 + 1))) <= (not (x in range(47, 115 + 1))))):
                f = False
        if f:
            l.append(a_max - a_min)
print(min(l))
