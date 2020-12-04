from typing import List
from functools import reduce


def trees_hit_for_slope(steps_right: int, steps_down: int, map: List[str]) -> int:
    trees_hit = 0
    for i in range(0, len(map), steps_down):
        if map[i][(steps_right * i) % len(map[0])] == "#":
            trees_hit += 1
    return trees_hit


if __name__ == '__main__':
    with open('inputs/i03.txt', 'r') as f:
        map = [line.strip() for line in f.readlines()]
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        results = [trees_hit_for_slope(right, down, map)
                   for (right, down) in slopes]
        product = reduce(lambda x, y: x * y, results)

        print("part 1:", trees_hit_for_slope(3, 1, map))
        print("part 2", product)


def part1():
    with open('inputs/i03.txt', 'r') as f:
        map = [line.strip() for line in f.readlines()]
        return trees_hit_for_slope(3, 1, map)


def part2():
    with open('inputs/i03.txt', 'r') as f:
        map = [line.strip() for line in f.readlines()]
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        results = [trees_hit_for_slope(right, down, map)
                   for (right, down) in slopes]
        return reduce(lambda x, y: x * y, results)
