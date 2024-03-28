def game1(heap, moves, to):
    if heap >= 29:
        return moves % 2 == to % 2
    if moves == to:
        return False

    h = [game1(heap + 1, moves + 1, to), game1(heap * 2, moves + 1, to)]
    return any(h)


def game2(heap, moves, to):
    if heap >= 29:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game2(heap + 1, moves + 1, to), game2(heap * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'19: {[s for s in range(1, 29) if not game2(s, 0, 1) and game2(s, 0, 2)]}')
print(f'20{[s for s in range(1,29) if not game2(s,0,1) and game2(s,0,3)]}')
print(f'21{[s for s in range(1,29) if game2(s,0,4)]}')