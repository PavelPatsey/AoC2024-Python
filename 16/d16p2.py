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
    min_score = None
    min_cases = []
    sr, sc = get_start(grid)
    visited = set()
    queue = [(0, sr, sc, 0, 1, frozenset({(sr, sc)}))]

    while queue:
        score, r, c, dr, dc, points = heapq.heappop(queue)
        visited.add((r, c, dr, dc))
        if grid[r][c] == "E":
            if min_score is None:
                min_score = score
            if score == min_score:
                min_cases.append((score, points))
                continue
            break
        for new_score, nr, nc, ndr, ndc, new_points in [
            (score + 1, r + dr, c + dc, dr, dc, points | {(r + dr, c + dc)}),
            (score + 1000, r, c, dc, -dr, points),
            (score + 1000, r, c, -dc, dr, points),
        ]:
            if grid[nr][nc] != "#" and (nr, nc, ndr, ndc) not in visited:
                heapq.heappush(queue, (new_score, nr, nc, ndr, ndc, new_points))

    all_min_points = {point for _, points in min_cases for point in points}
    return len(all_min_points)


def main():
    grid = get_data("input.txt")
    print("ans =", get_answer(grid))


if __name__ == "__main__":
    cProfile.run("main()")
