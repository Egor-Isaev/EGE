c = 0
for l1 in '1357':
    for l2 in '2468':
        for l3 in '1357':
            for l4 in '2468':
                for l5 in '1357':
                    for l6 in '2468':
                        for l7 in '1357':
                            for l8 in '2468':
                                for l9 in '1357':
                                    for l10 in '2468':
                                        for l11 in '1357':
                                            l = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 + l11
                                            if l.count('1') <= 4 and l.count('2') <= 4 and l.count(
                                                    '3') <= 4 and l.count('4') <= 4 and l.count('5') <= 4 and l.count(
                                                    '6') <= 4 and l.count('7') <= 4 and l.count('8') <= 4:
                                                c += 1

print(c)
