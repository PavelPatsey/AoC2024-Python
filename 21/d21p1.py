NUM_KP = [
    "789",
    "456",
    "123",
    "#0A",
]

DIR_KP = [
    "#^A",
    "<v>",
]

START_POSE = {
    NUM_KP: (3, 2),
    DIR_KP: (0, 0),
}


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def in_keypad(r, c, keypad):
    rows = len(keypad)
    cols = len(keypad[0])
    return 0 <= r < rows and 0 <= c < cols


def find(seq, keypad):
    pass


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    codes = get_data(file)
    print(codes)
    print(get_answer(codes))


if __name__ == "__main__":
    main()
