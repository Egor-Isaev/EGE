def f1(heap1, heap2, moves, to):
    if heap1 + heap2 > 80:
        return moves % 2 == to % 2
    if moves == to:
        return False
    if heap1 < heap2:
        h = [f1(heap1 + 1, heap2, moves + 1, to), f1(heap1 + 2, heap2, moves + 1, to),
             f1(heap1 * 2, heap2, moves + 1, to)]
    if heap2 < heap1:
        h = [f1(heap1, heap2 + 1, moves + 1, to), f1(heap1, heap2 + 2, moves + 1, to),
             f1(heap1, heap2 * 2, moves + 1, to)]
    return any(h)


def f2(heap1, heap2, moves, to):
    if heap1 + heap2 > 80:
        return moves % 2 == to % 2
    if moves == to:
        return False
    if heap1 < heap2:
        h = [f2(heap1 + 1, heap2, moves + 1, to), f2(heap1 + 2, heap2, moves + 1, to), f2(heap1 * 2, heap2, moves + 1, to)]
    else:
        h = [f2(heap1, heap2 + 1, moves + 1, to), f2(heap1, heap2 + 2, moves + 1, to), f2(heap1, heap2 * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'19: {min(s for s in range(1, 69) if not f2(12, s, 0, 1) and f2(12, s, 0, 2))}')
print(f'20: {min(s for s in range(1, 69) if not f2(12, s, 0, 1) and f2(12, s, 0, 3)), max(s for s in range(1, 69) if not f2(12, s, 0, 1) and f2(12, s, 0, 3))}')
print(f'21: {max(s for s in range(1, 69) if not f2(12, s, 0, 2) and f2(12, s, 0, 4))}')
