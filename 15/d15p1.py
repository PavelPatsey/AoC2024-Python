from copy import deepcopy

DIRS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
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
            raise Exception(f"invalid case! {grid[nr][nc]=}")

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


def main():
    grid, moves = get_data("input.txt")
    start = get_start(grid)

    ans = get_answer(grid, moves, start)
    print(f"{ans=}")


if __name__ == "__main__":
    main()
