def read_as_list(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
