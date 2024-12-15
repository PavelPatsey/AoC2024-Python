from copy import deepcopy

DIRS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

CONVERTS = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
}


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    grid, moves = data.split("\n\n")
    grid = grid.split()
    grid = [[x for x in line] for line in grid]
    moves = moves.strip()
    moves = "".join(moves.split())
    return grid, moves


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()
    return


def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                return r, c
    return


def convert(grid, move, node):
    dir = DIRS[move]

    def do_move(pos):
        r, c = pos
        dr, dc = dir
        nr, nc = r + dr, c + dc
        new_pos = nr, nc
        if grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            return True
        elif grid[nr][nc] == "O":
            moved = do_move(new_pos)
            if moved:
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                return True
            return False
        elif grid[nr][nc] == "#":
            return False
        else:
            raise Exception("invalid case!")

    is_moved = do_move(node)
    r, c = node
    new_node = node
    if is_moved:
        dr, dc = dir
        new_node = r + dr, c + dc
    return grid, new_node


def get_score(grid):
    res = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                res += r * 100 + c
    return res


def get_answer(grid, moves, start):
    node = start
    converted_grid = deepcopy(grid)
    for move in moves:
        converted_grid, node = convert(converted_grid, move, node)

    return get_score(converted_grid)


def get_extended_grid(grid):
    extended_grid = []
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        new_row = []
        for c in range(cols):
            node = grid[r][c]
            new_row.extend([x for x in CONVERTS[node]])
        extended_grid.append(new_row)
    return extended_grid


def get_pos_2(pos, grid):
    r, c = pos
    if grid[r][c] == "[":
        return r + 1, c
    elif grid[r][c] == "]":
        return r - 1, c
    else:
        raise Exception("Invalid case!")


def convert_2(grid, move, node):
    dir = DIRS[move]

    # "<" ">" "^" "v"

    def do_move(pos):
        r, c = pos
        dr, dc = dir
        nr, nc = r + dr, c + dc
        new_pos = nr, nc
        if grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            return True
        elif grid[nr][nc] in {"[", "]"}:
            pos_2 = get_pos_2(pos, grid)
            r2, c2 = pos_2
            nr2, nc2 = r2 + dr, c2 + dc
            new_pos_2 = nr2, nc2

            is_moved_1 = do_move(new_pos)
            is_moved_2 = do_move(new_pos_2)

            if is_moved_1 and is_moved_2:
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                grid[r2][c2], grid[nr2][nc2] = grid[nr2][nc2], grid[r2][c2]
                return True
            return False
        elif grid[nr][nc] == "#":
            return False
        else:
            raise Exception("invalid case!")

    is_moved = do_move(node)
    x, y = node
    new_node = node
    if is_moved:
        dx, dy = dir
        new_node = x + dx, y + dy
    return grid, new_node


def get_answer_2(grid, moves):
    node = get_start(grid)
    print(f"{node=}")
    converted_grid = deepcopy(grid)
    for move in moves:
        converted_grid, node = convert_2(converted_grid, move, node)
        print_grid(converted_grid)

    return get_score(converted_grid)


def main():
    grid, moves = get_data("input_2_part.txt")
    # start = get_start(grid)
    #
    # ans1 = get_answer(grid, moves, start)
    # print(f"{ans1=}")

    extended_grid = get_extended_grid(grid)

    print("Initial state:")
    print_grid(extended_grid)

    ans2 = get_answer_2(extended_grid, moves)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
