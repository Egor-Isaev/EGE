# x - из чего получаем
# y - что хотим получить
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 3, y)

# Ограничение "траектория содержит число n"
print(f(2, 26) * f(26, 87))