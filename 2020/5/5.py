def get_seat_id(tag: str) -> int:
    return int(tag[:7], 2) * 8 + int(tag[7:], 2)

def find_empty_seat(ids: [int]) -> int:
    ids = sorted(ids)
    return next(pass_id for i, pass_id in enumerate(ids) if (i < len(ids)-1 and pass_id + 1 != ids[i + 1])) + 1

if __name__ == "__main__":
    with open('input.in', 'r') as pass_file:
        passes = pass_file.read().replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0').split('\n')[:-1]
        ids = [get_seat_id(tag) for tag in passes]
        print(max(ids))
        print(find_empty_seat(ids))
