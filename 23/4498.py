


def f(x, y, k1, k2, k3):
    if x > y:
        return 0
    if x == y:
        return k1 <= 4 and k2 >= 2 and k3 == 5
    return f(x * 5, y, k1+1, k2, k3) + f(x * 3, y, k1, k2+1, k3) + f(x + 45, y, k1, k2, k3+1)


print(f(1, 2970,0,0,0))
