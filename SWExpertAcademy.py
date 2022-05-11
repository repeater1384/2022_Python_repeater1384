T = int(input())
for t in range(1, T + 1):
    command = input()
    x, y = 0, 0
    dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    max_dixtance = 0
    for c in command * 4:
        dx, dy = dir_list[dir_idx]
        if c == 'S':
            x += dx
            y += dy
        elif c == 'L':
            dir_idx = (dir_idx - 1) % 4
        elif c == 'R':
            dir_idx = (dir_idx + 1) % 4
        distance = x * x + y * y
        max_dixtance = max(max_dixtance, distance)

    if x == y == 0:
        answer = max_dixtance
    else:
        answer = 'oo'
    print(f'#{t} {answer}')
