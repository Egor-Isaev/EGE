from fnmatch import fnmatch

for x in range(0, 10**10, 3013):
    if fnmatch(str(x), '1?6961*5'):
        print(x)
