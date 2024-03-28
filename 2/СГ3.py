print('x y w z')
for x in range (0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if ((x or y) <= (y and z)) and ((w == x) or (w <= (not(z)))):
                    print(x,y,w,z)
