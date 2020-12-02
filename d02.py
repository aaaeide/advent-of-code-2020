from typing import Tuple, List, Callable, Any
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


def indexed_reduce(
    function: Callable[[Any, Any, int], Any],
    sequence: List[Any],
    initial: Any = None,
    verbose: bool = False
) -> Any:
    """
    A reducer which gives the reduce function index as well, which functools.reduce
    annoyingly doesn't. Only accepts List as sequence.
    """
    if len(sequence) == 0:
        raise TypeError(
            "indexed_reduce() of empty iterable with no initial value")

    if initial == None:
        value = sequence[0]
    else:
        value = initial

    for i in range(len(sequence)):
        value = function(value, sequence[i], i)

        if verbose:
            print(f"{'='*20}\nsequence[{i}]: {sequence[i]}\nvalue: {value}")

    return value


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

    ct = reduce(ct_reduce(char), string, 0)

    return ct in range(min, max+1)


###########################
# Part 2: Check positions #
###########################


def poscheck_reduce(char: str, pos1: int, pos2: int) -> Callable[[bool, str, int], bool]:
    def red(acc: bool, cur: str, idx: int) -> bool:
        # XOR (^) because exactly one position has to match
        return acc ^ True if cur == char and idx in (pos1, pos2) else acc

    return red


def pos_check(parsed: ParsedLine) -> bool:
    ((pos1, pos2), char, string) = parsed

    return indexed_reduce(poscheck_reduce(char, pos1-1, pos2-1), list(string), False)


#####################
# Do the damn thing #
#####################


def check_lines(lines: List[str]) -> Tuple[int, int]:

    accepted1 = [line for line in lines if ct_check(parse_line(line))]
    accepted2 = [line for line in lines if pos_check(parse_line(line))]

    return (len(accepted1), len(accepted2))


print(check_lines(example))

with open('i02.txt', 'r') as f:
    print(check_lines(f.readlines()))
