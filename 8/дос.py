cnt = 0
for a1 in "АПРСУ":
    for a2 in "АПРСУ":
        for a3 in "АПРСУ":
            for a4 in "АПРСУ":
                for a5 in "АПРСУ":
                    a = a1 + a2 + a3 + a4 + a5
                    cnt += 1
                    if a.count('У') <= 1 and a.count('АА') == 0:
                        print(cnt)
