import re


def get_robots(input_file):
    def _get_robot(string):
        "p=0,4 v=3,-3"
        pattern = re.compile(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)")
        matches = pattern.findall(string)
        px, py, vx, vy = map(int, matches[0])
        return (px, py), (vx, vy)

    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [_get_robot(line) for line in data]


def get_answer(robots):
    return


def main():
    robots = get_robots("test_input")
    print(robots)
    print(get_answer(robots))


if __name__ == "__main__":
    main()
