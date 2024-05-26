def f1(heap, moves, to, i):
    if heap >= 21:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [f1(heap + 1, moves + 1, to), f1(heap + 2, moves + 1, to), f1(heap * 2, moves + 1, to)]
    return any(h)


def f2(heap, moves, to, i):
    if heap >= 21:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [f2(heap + 1, moves + 1, to), f2(heap + 2, moves + 1, to), f2(heap * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'19: {min(s for s in range(1, 21) if not f1(s, 0, 1) and f1(s, 0, 3))}')
print(
    f'20: {min(s for s in range(1, 21) if not f2(s, 0, 2) and f2(s, 0, 4)), max(s for s in range(1, 21) if not f2(s, 0, 2) and f2(s, 0, 4))}')
print(f'21: {max(s for s in range(1, 21) if not f2(s, 0, 1) and not f2(s, 0, 3) and f2(s, 0, 5))}')
