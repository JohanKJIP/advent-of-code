
def get_seat(tag: str, row_start=0, row_end=127, col_start=0, col_end=7) -> (int, int):
    if tag[0] == 'F':
        if len(tag) == 1: return row_start, col_start 
        return get_seat(tag[1:], row_start, row_start + (row_end - row_start)//2, col_start, col_end)
    elif tag[0] == 'B':
        if len(tag) == 1: return row_end, col_start
        return get_seat(tag[1:], row_start + (row_end - row_start + 1)//2, row_end, col_start, col_end)
    if tag[0] == 'L':
        if len(tag) == 1: return row_start, col_start 
        return get_seat(tag[1:], row_start, row_end, col_start, col_start + (col_end - col_start)//2)
    elif tag[0] == 'R':
        if len(tag) == 1: return row_start, col_end
        return get_seat(tag[1:], row_start, row_end, col_start + (col_end - col_start + 1)//2, col_end)

def seat_id(seat: (int, int)) -> int:
    return seat[0] * 8 + seat[1]

def find_seat(ids) -> (int, int):
    prev_id = ids[0]
    for pass_id in sorted(ids):
        if pass_id - prev_id > 1:
            return prev_id + 1
        prev_id = pass_id

if __name__ == "__main__":
    with open('input.in', 'r') as pass_file:
        passes = pass_file.read().split('\n')[:-1]
        ids = [seat_id(get_seat(tag)) for tag in passes]
        print(max(ids))
        print(find_seat(ids))
