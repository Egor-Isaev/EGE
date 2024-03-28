def game1(heap, moves, to, i):
    if heap >= 34:
        return moves % 2 == to % 2
    if moves == to:
        return False
    if i == 1:
        h = [game1(heap + 2, moves + 1, to, 2), game1(heap * 2, moves + 1, to, 3)]
    elif i == 2:
        h = [game1(heap + 1, moves + 1, to, 1), game1(heap * 2, moves + 1, to, 3)]
    elif i == 3:
        h = [game1(heap + 2, moves + 1, to, 2), game1(heap * 2, moves + 1, to, 3)]
    else:
        h = [game1(heap + 1, moves + 1, to, 1), game1(heap + 2, moves + 1, to, 2), game1(heap * 2, moves + 1, to, 3)]
    return any(h)


def game2(heap, moves, to, i):
    if heap >= 34:
        return moves % 2 == to % 2
    if moves == to:
        return False
    if i == 1:
        h = [game2(heap + 2, moves + 1, to, 2), game2(heap * 2, moves + 1, to, 3)]
    elif i == 2:
        h = [game2(heap + 1, moves + 1, to, 1), game2(heap * 2, moves + 1, to, 3)]
    elif i == 3:
        h = [game2(heap + 1, moves + 1, to, 1), game2(heap + 2, moves + 1, to, 2), ]
    else:
        h = [game2(heap + 1, moves + 1, to, 1), game2(heap + 2, moves + 1, to, 2), game2(heap * 2, moves + 1, to, 3)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)
print(f'19:{[s for s in range(1,34) if not game2(s,0,1,0) and game2(s,0,2,0)]}')
print(f'20:{[s for s in range(1,34) if not game2(s,0,1,0) and game2(s,0,3,0)]}')
print(f'21:{[s for s in range(1,34) if not game2(s,0,2,0) and game2(s,0,4,0)]}')