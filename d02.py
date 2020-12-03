from typing import Tuple, List, Callable
from functools import reduce

example = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]

ParsedLine = Tuple[Tuple[int, int], str, str]


def parse_line(line: str) -> ParsedLine:
    """ min-max char: string """
    splt = line.strip().split(' ')
    [min, max] = [int(i) for i in splt[0].split('-')]
    char = splt[1][0]  # Drop ':'
    string = splt[2]

    return ((min, max), char, string)


def ct_reduce(char: str) -> Callable[[int, str], int]:
    def red(acc: int, cur: str) -> int:
        return acc + 1 if cur == char else acc

    return red


def ct_check(parsed: ParsedLine) -> bool:
    ((min, max), char, string) = parsed

    return reduce(ct_reduce(char), string, 0) in range(min, max+1)


def pos_check(parsed: ParsedLine) -> bool:
    (positions, char, string) = parsed

    return reduce(lambda x, y: x ^ y, [string[pos-1] == char for pos in positions])


def part1():
    with open('i02.txt', 'r') as f:
        return len([line for line in f.readlines() if ct_check(parse_line(line))])


def part2():
    with open('i02.txt', 'r') as f:
        return len([line for line in f.readlines() if pos_check(parse_line(line))])


if __name__ == "__main__":
    print(f'PART 1:\t{part1()}')
    print(f'PART 2:\t{part2()}')
