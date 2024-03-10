from fnmatch import fnmatch
for x in range(0,10**8,2023):
    if fnmatch(str(x),'3?1*57'):
        print(x,x//2023)
