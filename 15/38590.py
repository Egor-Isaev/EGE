l = []
for a_min in range(-200, 200):
    for a_max in range(a_min+1, 200):
        f = True
        for x in range(200):
            if not((x in range(17, 59)) <= (
                    ((x not in range(29, 81)) and (x not in range(a_min, a_max))) <= (x not in range(17, 59)))):
                f = False
        if f:
            l.append(a_max - a_min)
print(min(l))
