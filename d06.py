from functools import reduce
from typing import Tuple


def solve(inp: str) -> Tuple[int, int]:
    groups = [group.lower().strip().split("\n")
              for group in inp.split("\n\n")]

    any_answered = [reduce(lambda acc, cur: acc.union(cur),
                           [set(person) for person in group])
                    for group in groups]
    everyone_answered = [reduce(lambda acc, cur: acc.intersection(cur),
                                [set(person) for person in group])
                         for group in groups]

    sum_any_answered = reduce(
        lambda acc_sum, cur_set: acc_sum + len(cur_set), any_answered, 0)
    sum_everyone_answered = reduce(
        lambda acc_sum, cur_set: acc_sum + len(cur_set), everyone_answered, 0)

    return sum_any_answered, sum_everyone_answered


if __name__ == '__main__':
    with open('inputs/i06.txt', 'r') as f:
        inp = f.read()
        print("PART 1:", solve(inp))
