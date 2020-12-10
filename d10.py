from typing import List

ex1 = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
ex2 = [1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24,
       25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]


def greedy_longest_path(adaps: List[int]) -> int:
    # There are no "blind alleys" – paths from which we cannot reach the
    # goal – the correct solution is to always GREEDILY choose the next adap with
    # the lower joltage.
    adapset = set(adaps)  # No duplicates in input or example
    joltage = 0
    diffs = [0, 0, 1]  # we always add a 3-diff at the end
    while len(adapset):
        next_adap = min(adapset.intersection(
            set([joltage + i for i in range(1, 4)])))
        diffs[next_adap - joltage - 1] += 1
        joltage = next_adap
        adapset.remove(next_adap)  # throws if we did not find an adap
    return diffs[0] * diffs[2]


def find_num_paths(adaps: List[int]) -> int:
    # For each adap (node in a digraph from 0 to device's joltage), the
    # number of paths to the goal is the sum of the number of paths from
    # each adap reachable from the current adap. The problem exhibits
    # OPTIMAL SUBSTRUCTURE – an optimal solution is composed from optimal
    # solutions to related, independently solvable subproblems.
    adapset = set(adaps)
    memo = [0] * (max(adapset) + 1)

    def find_num_paths_from(frm: int) -> int:
        if memo[frm] != 0:
            return memo[frm]

        res = 0
        reachable_adaps = adapset.intersection(
            set([frm + i for i in range(1, 4)]))

        # base case – final adap:
        if len(reachable_adaps) == 0:
            res = 1
        else:
            res = sum([find_num_paths_from(adap) for adap in reachable_adaps])

        memo[frm] = res
        return res

    return find_num_paths_from(0)


if __name__ == '__main__':
    with open('inputs/i10.txt', 'r') as f:
        adaps = [int(line) for line in f.readlines()]

        print("PART 1:")
        print("EXAMPLE 1", greedy_longest_path(ex1))
        print("EXAMPLE 2", greedy_longest_path(ex2))
        print("GIVEN INPUT", greedy_longest_path(adaps))

        print("\nPART 2:")
        print("EXAMPLE 1", find_num_paths(ex1))
        print("EXAMPLE 2", find_num_paths(ex2))
        print("GIVEN INPUT", find_num_paths(adaps))
