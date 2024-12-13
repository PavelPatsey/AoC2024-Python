from day_12 import DIRS4, get_grid, get_perimeter, get_plots_bfs


def rotate_clockwise(dir):
    return dir[1], -dir[0]


def rotate_counterclockwise(dir):
    return -dir[1], dir[0]


def get_half_of_corners_count(plot, dir, plot_set):
    """
    Рассмотрим ноду А, и ноды: сверху, справа, по диагонали
    0) если есть верхняя нода, тогда нет углов
    1) если все ноды не входят в сет, тогда будет угол

    _.
    A|

    2) если диагональный элемент в сете, тогда будет угол

    01  _#  _#
    А2  A#  A|

    если есть угол добавляем 1/2, так как он будет рассмотрен еще раз,
    потому что один угол принадлежит двум сторонам
    """
    r, c = plot
    dr, dc = dir
    r0, c0 = r + dr, c + dc

    if (r0, c0) in plot_set:
        return 0

    res = 0
    for dir2 in (rotate_clockwise(dir), rotate_clockwise(dir)):
        dr2, dc2 = dir2
        r2, c2 = r + dr2, c + dc2
        r1, c1 = r + dr + dr2, c + dc + dc2
        nodes = ((r0, c0), (r1, c1), (r2, c2))
        mapped = map(lambda x: x in plot_set, nodes)
        if sum(mapped) == 0 or (r1, c1) in plot_set:
            res += 1 / 2

    return res


def get_corners_number(plot_set):
    res = 0
    for plot in plot_set:
        for dir in DIRS4:
            res += get_half_of_corners_count(plot, dir, plot_set)
    return int(res)


def main():
    file = "input"
    grid = get_grid(file)

    plots = get_plots_bfs(grid)
    ans1_bfs = sum(map(lambda x: len(x) * get_perimeter(grid, x), plots.values()))
    print(ans1_bfs)

    ans2 = sum(map(lambda x: len(x) * get_corners_number(x), plots.values()))
    print(ans2)

    if file == "test_input_1":
        assert ans1_bfs == 140
        assert ans2 == 80
    elif file == "test_input_2":
        assert ans1_bfs == 772
        assert ans2 == 436
    elif file == "test_input_larger":
        assert ans1_bfs == 1930
        assert ans2 == 1206
    elif file == "input":
        assert ans1_bfs == 1424006
        assert ans2 == 858684
    else:
        raise Exception("unknown input!")


if __name__ == "__main__":
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

    assert rotate_clockwise(LEFT) == UP
    assert rotate_clockwise(UP) == RIGHT
    assert rotate_clockwise(RIGHT) == DOWN
    assert rotate_clockwise(DOWN) == LEFT

    assert rotate_counterclockwise(LEFT) == DOWN
    assert rotate_counterclockwise(DOWN) == RIGHT
    assert rotate_counterclockwise(RIGHT) == UP
    assert rotate_counterclockwise(UP) == LEFT

    assert get_corners_number({(2, 3), (1, 2), (3, 3), (2, 2)}) == 8

    main()
