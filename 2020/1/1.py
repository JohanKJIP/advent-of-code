
def sum_two(target: int) -> int:
    with open('input.in', 'r') as expense_report:
        numbers = [int(line) for line in expense_report]

        # O(n)
        lookup = {}
        for number in numbers:
            if target - number in lookup:
                return number * (target - number)
            lookup[number] = 1

def sum_three(target: int) -> int:
    with open('input.in', 'r') as expense_report:
        numbers = [int(line) for line in expense_report]

        # O(n^2)
        for a in numbers:
            lookup = {}
            left = target - a
            for b in numbers:
                if left - b in lookup:
                    return a * b * (left - b)
                lookup[b] = 1

if __name__ == "__main__":
    print(f'You get {sum_two(target=2020)}')
    print(f'You get {sum_three(target=2020)}')