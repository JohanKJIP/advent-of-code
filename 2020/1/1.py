
def task_one(target: int) -> int:
    with open('1.in', 'r') as expense_report:
        numbers = [int(line) for line in expense_report]

        # O(n)
        lookup = {}
        for number in numbers:
            if target - number in lookup:
                return number * (target - number)
            lookup[number] = 1

def task_two(target: int) -> int:
    with open('1.in', 'r') as expense_report:
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
    print(f'You get {task_one(target=2020)}')
    print(f'You get {task_two(target=2020)}')