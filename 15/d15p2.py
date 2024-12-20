import cProfile
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


def in_grid(node, grid):
    r, c = node
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_box(node, grid):
    r, c = node
    if grid[r][c] == "[":
        left = r, c
        right = r, c + 1
    elif grid[r][c] == "]":
        right = r, c
        left = r, c - 1
    else:
        raise Exception(f"invalid case! {grid[r][c]=}")
    return left, right


def convert(grid, move, node):
    dir = DIRS[move]
    dr, dc = dir
    movable_boxes = []

    def _move_box(box):
        left, right = box
        if move == "<":
            next_node = left[0] + dir[0], left[1] + dir[1]
            for n, ch in zip([next_node, left, right], ["[", "]", "."]):
                r, c = n
                grid[r][c] = ch
        elif move == ">":
            next_node = right[0] + dir[0], right[1] + dir[1]
            for n, ch in zip([left, right, next_node], [".", "[", "]"]):
                r, c = n
                grid[r][c] = ch
        elif move in {"^", "v"}:
            next_left = left[0] + dir[0], left[1] + dir[1]
            next_right = right[0] + dir[0], right[1] + dir[1]
            for n, ch in zip(
                [left, right, next_left, next_right],
                [".", ".", "[", "]"],
            ):
                r, c = n
                grid[r][c] = ch
        else:
            raise Exception(f"invalid case! {move=}")

    def _is_available_node(node):
        r, c = node
        if grid[r][c] == ".":
            return True
        elif grid[r][c] == "#":
            return False
        elif grid[r][c] in {"[", "]"}:
            box = get_box(node, grid)
            if _is_movable_box(box):
                if box not in movable_boxes:
                    movable_boxes.append(box)
                return True
        else:
            raise Exception(f"invalid case! {grid[r][c]=}")

    def _is_movable_box(box):
        left, right = box
        if move == "<":
            next_left = left[0] + dir[0], left[1] + dir[1]
            nodes_to_check = [next_left]
        elif move == ">":
            next_right = right[0] + dir[0], right[1] + dir[1]
            nodes_to_check = [next_right]
        elif move in {"^", "v"}:
            next_left = left[0] + dir[0], left[1] + dir[1]
            next_right = right[0] + dir[0], right[1] + dir[1]
            nodes_to_check = [next_left, next_right]
        else:
            raise Exception(f"invalid case! {move=}")
        return all(map(_is_available_node, nodes_to_check))

    def _is_moved(pos):
        r, c = pos
        dr, dc = dir
        nr, nc = r + dr, c + dc
        new_pos = nr, nc
        if grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            return True
        elif grid[nr][nc] in {"[", "]"}:
            box = get_box(new_pos, grid)
            if _is_movable_box(box):
                if box not in movable_boxes:
                    movable_boxes.append(box)
                for b in movable_boxes:
                    _move_box(b)
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                return True
            return False
        elif grid[nr][nc] == "#":
            return False
        else:
            raise Exception(f"invalid case! {grid[nr][nc]=}")

    is_moved = _is_moved(node)

    r, c = node
    new_node = node
    if is_moved:
        nr, nc = r + dr, c + dc
        new_node = nr, nc
    return grid, new_node


def get_score(grid):
    res = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "[":
                res += r * 100 + c
    return res


def get_answer(grid, moves):
    node = get_start(grid)
    converted_grid = deepcopy(grid)
    for move in moves:
        converted_grid, node = convert(converted_grid, move, node)
    return get_score(converted_grid)


def main():
    grid, moves = get_data("input.txt")
    extended_grid = get_extended_grid(grid)
    ans2 = get_answer(extended_grid, moves)
    print(f"{ans2=}")


if __name__ == "__main__":
    cProfile.run("main()")
