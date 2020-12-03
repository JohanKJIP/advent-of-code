import math


def count_trees(maps, right: int, down: int) -> int:
    return [maps[step*down][step*right % len(maps[0])] for step in range(0, len(maps)//down)].count('#')


def multiply_slopes(maps, slopes):
    return math.prod([count_trees(maps, step_dir[0], step_dir[1]) for step_dir in slopes])


if __name__ == "__main__":
    with open('input.in', 'r') as map_file:
        
        maps = []
        for line in map_file:
            maps.append([char for char in line.replace('\n', '')])
        print(f'Number of trees: {count_trees(maps, 3, 1)}')

        # multiply slopes 
        print(multiply_slopes(maps, [(1,1),(3,1),(5,1),(7,1),(1,2)]))
