print('x y w u z')
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for u in range(0, 2):
                for z in range(0, 2):
                    if (not(((z <= w) and (y == (not(x))))<=(u ==(y or z)))):
                        print(x,y,w,u,z)
