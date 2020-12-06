
def count_or_yes(groups: [str]) -> int:
    return sum((len(set(group[0])) for group in groups))

def count_and_yes(groups: [str]) -> int:
    [len(group[1]) for group in groups if len(for char in group[0]) == 0]

if __name__ == "__main__":
    with open('input.in', 'r') as f:
        groups = [('', 0)]
        for line in f:
            if line == '\n':
                groups.append(('', 0))
            groups[-1] = (groups[-1][0] + line.rstrip(), line.rstrip())

        print(count_or_yes(groups))
        print(count_and_yes(groups))