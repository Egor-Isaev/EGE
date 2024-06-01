cnt = 0
for a1 in "МИТРОФАН":
    for a2 in "МИТРОФАН":
        for a3 in "МИТРОФАН":
            for a4 in "МИТРОФАН":
                for a5 in "МИТРОФАН":
                    for a6 in "МИТРОФАН":
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if (a.count('М') <= 1 and a.count('И') <= 1 and a.count('Т') <= 1 and a.count(
                            'Р') <= 1 and a.count('О') <= 1 and a.count('Ф') <= 1 and a.count('А') <= 1 and a.count(
                            'Н') <= 1) and (a.count('М') + a.count('Т') + a.count('Р') + a.count('Ф') + a.count('Н') > a.count('И') + a.count('А') + a.count('О')) and (a.count('ИИ') + a.count('ИО') + a.count('ИА') + a.count('ОИ') + a.count('ОА') + a.count('ОО') + a.count('АИ') + a.count('АО') + a.count('АА') == 0):
                            cnt += 1
print(cnt)
