from typing import Tuple, List, Callable
from functools import reduce

example = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]

###################
# HELPERS         #
###################

ParsedLine = Tuple[Tuple[int, int], str, str]


def parse_line(line: str) -> ParsedLine:
    """ min-max char: string """
    splt = line.strip().split(' ')
    [min, max] = [int(i) for i in splt[0].split('-')]
    char = splt[1][0]  # Drop ':'
    string = splt[2]

    return ((min, max), char, string)

########################
# Part 1: Check count  #
########################


def ct_reduce(char: str) -> Callable[[int, str], int]:
    def red(acc: int, cur: str) -> int:
        return acc + 1 if cur == char else acc

    return red


def ct_check(parsed: ParsedLine) -> bool:
    ((min, max), char, string) = parsed

    return reduce(ct_reduce(char), string, 0) in range(min, max+1)

###########################
# Part 2: Check positions #
###########################


def pos_check(parsed: ParsedLine) -> bool:
    (positions, char, string) = parsed

    return reduce(lambda x, y: x ^ y, [string[pos-1] == char for pos in positions])

#####################
# Do the damn thing #
#####################


def check_lines(lines: List[str]) -> Tuple[int, int]:

    accepted1 = [line for line in lines if ct_check(parse_line(line))]
    accepted2 = [line for line in lines if pos_check(parse_line(line))]

    return (len(accepted1), len(accepted2))


with open('i02.txt', 'r') as f:
    print('EXPECTED:\n(2,1)\n(536,558)\n\nACTUAL:')
    print(check_lines(example))
    print(check_lines(f.readlines()))
