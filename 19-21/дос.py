def f1(heap1, heap2, moves, to):
    if heap1 + heap2 >= 123:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [f1(heap1 + 1, heap2, moves + 1, to), f1(heap1 * 2, heap2, moves + 1, to),f1(heap1, heap2 + 1, moves + 1, to), f1(heap1, heap2 * 2, moves + 1, to)]
    return any(h)


def f2(heap1, heap2, moves, to):
    if heap1 + heap2 >= 123:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [f2(heap1 + 1, heap2, moves + 1, to), f2(heap1 * 2, heap2, moves + 1, to),f2(heap1, heap2 + 1, moves + 1, to), f2(heap1, heap2 * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print('19:', min(s for s in range(1, 110) if not f1(13, s, 0, 1) and f1(13, s, 0, 2)))
print('20:', sorted(s for s in range(1, 110) if not f2(13, s, 0, 1) and f2(13, s, 0, 3)))
print('21:', min(s for s in range(1, 110) if not f2(13, s, 0, 2) and f2(13, s, 0, 4)))
