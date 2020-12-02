
def task_one() -> int:
    with open('2.in', 'r') as password_file:
        valid = 0
        for line in password_file:
            # parse line
            line = line.split(' ')
            min_appear, max_appear = map(lambda x: int(x), line[0].split('-'))
            letter = line[1].replace(':', '')
            password = line[2]

            # evaluate validity
            occurance = password.count(letter)
            if occurance >= min_appear and occurance <= max_appear:
                valid += 1
        return valid


def task_two() -> int:
    with open('2.in', 'r') as password_file:
        valid = 0
        for line in password_file:
            # parse line
            line = line.split(' ')
            first_idx, second_idx = map(lambda x: int(x)-1, line[0].split('-'))
            letter = line[1].replace(':', '')
            password = line[2].replace('\n', '')

            # evaluate validity
            if (password[first_idx] == letter) != (password[second_idx] == letter):
                valid += 1
        return valid


if __name__ == "__main__":
    print(f'Task 1: valid passwords {task_one()}')
    print(f'Task 2: valid passwords {task_two()}')
