import cProfile
import heapq


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in line] for line in data]


def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                return r, c
    return


def get_answer(grid):
    res = []
    sr, sc = get_start(grid)
    visited = set()
    queue = [(0, sr, sc, 0, 1)]

    while queue:
        score, r, c, dr, dc = heapq.heappop(queue)
        visited.add((r, c, dr, dc))
        if grid[r][c] == "E":
            res.append(score)
        for new_score, nr, nc, ndr, ndc in [
            (score + 1, r + dr, c + dc, dr, dc),
            (score + 1000, r, c, dc, -dr),
            (score + 1000, r, c, -dc, dr),
        ]:
            if grid[nr][nc] != "#" and (nr, nc, ndr, ndc) not in visited:
                heapq.heappush(queue, (new_score, nr, nc, ndr, ndc))

    return min(res)


def main():
    grid = get_data("input.txt")
    print("ans =", get_answer(grid))


if __name__ == "__main__":
    cProfile.run("main()")
