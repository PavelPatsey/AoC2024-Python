import cProfile
import sys

sys.setrecursionlimit(5_000)


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in line] for line in data]


def rotate_clockwise(dir):
    return dir[1], -dir[0]


def rotate_counterclockwise(dir):
    return -dir[1], dir[0]


def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                return r, c
    return


def get_answer(grid):
    scores = []

    def dfs(node, dir, score, visited):
        r, c = node
        if grid[r][c] == "E":
            print(f"{scores=}")
            print(f"{visited=}")
            print("===")
            scores.append(score)
            return
        elif grid[r][c] == "#" or node in visited:
            return

        visited = visited | {node}

        dirs = [dir, rotate_clockwise(dir), rotate_counterclockwise(dir)]
        d_scores = [1, 1_001, 1_001]
        for dir, ds in zip(dirs, d_scores):
            dr, dc = dir
            new_node = r + dr, c + dc
            new_score = score + ds
            dfs(new_node, dir, new_score, visited)

    start = get_start(grid)
    dir = (0, 1)
    dirs = [
        dir,
        rotate_clockwise(dir),
        rotate_counterclockwise(dir),
        (-dir[0], -dir[1]),
    ]
    r, c = start
    for dir, score in zip(dirs, [1, 1_001, 1_001, 2_001]):
        dr, dc = dir
        new_node = r + dr, c + dc
        dfs(new_node, dir, score, {start})

    print(f"{scores=}")
    return min(scores)


def main():
    grid = get_data("input_small.txt")
    print("ans =", get_answer(grid))


if __name__ == "__main__":
    cProfile.run("main()")
