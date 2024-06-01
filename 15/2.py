l = []
for a_min in range(-200, 200):
    for a_max in range(a_min+1, 200):
        f = True
        for x in range(200):
            if not ((x in range(47, 115 + 1)) <= (((x not in range(a_min, a_max)) and (x in range(24, 90 + 1))) <= (
            (x not in range(47, 115 + 1))))):
                f = False
        if f:
            l.append(a_max - a_min)
print(min(l))
