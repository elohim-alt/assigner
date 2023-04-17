def read_as_list(filename: str):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
