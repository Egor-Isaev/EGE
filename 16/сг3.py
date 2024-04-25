
def f(a, b):
    if b == 0:
        return 0
    if b > 0 and b % 2 == 0:
        return 2*f(a,b/2)
    if b % 2 != 0:
        return a + f(a,b-1)

for y in range(1,90000):
    if 89999 % y == 0:
        print(89999//301)
