def f(heap, moves, to):
    if heap >= 48:
        return moves % 2 == to % 2
    if moves==to:
        return 0
    h = [f(heap + 1, moves + 1, to), f(heap + 3, moves + 1, to), f(heap * 2, moves + 1, to)]
    return any(h)


def f2(heap, moves, to):
    if heap >= 48:
        return moves % 2 == to % 2
    if moves==to:
        return 0
    h = [f2(heap + 1, moves + 1, to), f2(heap + 3, moves + 1, to), f2(heap * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print('Задание 19', min(s for s in range(1, 48) if not f(s, 0, 1) and f(s, 0, 2)))
print('Задание 20', [s for s in range(1, 48) if not f2(s, 0, 1) and f2(s, 0, 3)])
print('Задание 21', min(s for s in range(1, 48) if f2(s, 0, 4) and not f2(s, 0, 2)))

