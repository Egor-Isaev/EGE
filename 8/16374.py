cnt = 0
for a1 in '123456':
    for a2 in '0123456':
        for a3 in '0123456':
            for a4 in '0123456':
                for a5 in '0123456':
                    for a6 in '0123456':
                        for a7 in '0123456':
                            a = a1 + a2 + a3 + a4 + a5 + a6 + a7
                            if a.count('0') + a.count('2') + a.count('4') + a.count('6') == 2:
                                cnt += 1
print(cnt)
