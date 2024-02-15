# Ограничение "никакая команда не повторяется более двух раз подряд"
def f(x, y, cur, pre):
    if x > y:
        return 0
    if x == y:
        return 1
    if cur == pre == '+':
        return f(x * 2, y, '*', cur)
    elif cur == pre == '*':
        return f(x + 1, y, '+', cur)
    else:
        return f(x * 2, y, '*', cur) + f(x + 1, y, '+', cur)


print(f(1, 14, '', ''))