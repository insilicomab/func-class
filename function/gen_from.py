# リスト9.9
def read_files(*files):
    for file in files:
        yield from read_lines(file)


def read_lines(path):
    with open(path, "r", encoding="UTF-8") as file:
        for line in file:
            yield line.rstrip("\n")


if __name__ == "__main__":
    for line in read_files(
        "input/sample1.dat", "input/sample2.dat", "input/sample3.dat"
    ):
        print(line)
