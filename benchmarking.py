import timeit


def do_timeit(command, globals, number):
    return "{:.5f}".format(timeit.timeit(command, globals=globals, number=number)/number)


def d01():
    from d01 import part1 as d01p1, part2 as d01p2
    print("\nBENCHMARK DAY 01:")
    number = 100
    print(
        f"Ran part1() {number} times, average result: {do_timeit('d01p1()', locals(), number)} seconds")
    print(
        f"Ran part2() {number} times, average result: {do_timeit('d01p2()', locals(), number)} seconds")


def d02():
    from d02 import part1 as d02p1, part2 as d02p2
    print("\nBENCHMARK DAY 02:")
    number = 100
    print(
        f"Ran part1() {number} times, average result: { do_timeit('d02p1()', locals(), number)} seconds")
    print(
        f"Ran part2() {number} times, average result: {do_timeit('d02p2()', locals(), number)} seconds")


def d03():
    from d03 import part1 as d03p1, part2 as d03p2
    print("\nBENCHMARK DAY 03:")
    number = 100
    print(
        f"Ran part1() {number} times, average result: {do_timeit('d03p1()', locals(), number)} seconds")
    print(
        f"Ran part2() {number} times, average result: {do_timeit('d03p2()', locals(), number)} seconds")


def d04():
    from d04 import parse_and_count_valid
    print("\nBENCHMARK DAY 04:")
    number = 100
    with open('inputs/i04.txt', 'r') as f:
        inp = f.read()
        print(
            f"Ran parse_and_count_valid() {number} times, average result: {do_timeit('parse_and_count_valid(inp)', locals(), number)} seconds")


def d05():
    from d05 import max_seat_id, find_seat
    print("\nBENCHMARK DAY 05:")
    number = 100
    with open('inputs/i05.txt', 'r') as f:
        codes = [line.strip() for line in f.readlines()]
        print(
            f"Part 1: Ran max_seat_id() {number} times, average result: {do_timeit('max_seat_id(codes)', locals(), number)} seconds")
        print(
            f"Part 2: Ran find_seat() {number} times, average result: {do_timeit('find_seat(codes)', locals(), number)} seconds")


def d06():
    from d06 import solve
    print("\nBENCHMARK DAY 06:")
    number = 100
    with open('inputs/i06.txt', 'r') as f:
        inp = f.read()
        print(
            f"Ran solve() {number} times, average result: {do_timeit('solve(inp)', locals(), number)} seconds")


def d07():
    from d07 import part1 as d07p1, part2 as d07p2
    print("\nBENCHMARK DAY 07:")
    number = 100
    with open('inputs/i07.txt', 'r') as f:
        inp = f.read()
        print(
            f"Ran part1() {number} times, average result: {do_timeit('d07p1(inp)', locals(), number)} seconds")
        print(
            f"Ran part2() {number} times, average result: {do_timeit('d07p2(inp)', locals(), number)} seconds")


def d08():
    from d08 import part1 as d08p1, part2 as d08p2
    print("\nBENCHMARK DAY 08:")
    number = 100
    with open('inputs/i08.txt', 'r') as f:
        inp = f.read().strip()
        print(
            f"Ran part1() {number} times, average result: {do_timeit('d08p1(inp)', locals(), number)} seconds")
        print(
            f"Ran part2() {number} times, average result: {do_timeit('d08p2(inp)', locals(), number)} seconds")


def d09():
    from d09 import find_weird_sum, find_weird_num
    print("\nBENCHMARK DAY 09:")
    number = 100
    with open('inputs/i09.txt', 'r') as f:
        numbers = [int(line) for line in f.readlines()]
        print(
            f"PART 1: Ran find_weird_num() {number} times, average result: {do_timeit('find_weird_num(25, numbers)', locals(), number)} seconds")
        sol_p1 = find_weird_num(25, numbers)
        print(
            f"PART 2: Ran find_weird_sum() {number} times, average result: {do_timeit('find_weird_sum(sol_p1, numbers)', locals(), number)} seconds")


def d10():
    from d10 import greedy_longest_path, find_num_paths
    print("\nBENCHMARK DAY 10:")
    number = 100
    with open('inputs/i10.txt', 'r') as f:
        adaps = [int(line) for line in f.readlines()]
        print(
            f"PART 1: Ran greedy_longest_path() {number} times, average result: {do_timeit('greedy_longest_path(adaps)', locals(), number)} seconds")
        print(
            f"PART 2: Ran find_num_paths() {number} times, average result: {do_timeit('find_num_paths(adaps)', locals(), number)} seconds")


def d11():
    from d11 import solve
    print("\nBENCHMARK DAY 11:")
    number = 100
    with open('inputs/i11.txt', 'r') as f:
        map = f.read().strip().split("\n")
        print(
            f"PART 1: Ran solve() {number} times, average result: {do_timeit('solve(map, part=1)', locals(), number)} seconds")
        print(
            f"PART 2: Ran solve() {number} times, average result: {do_timeit('solve(map, part=2)', locals(), number)} seconds")


def d12():
    from d12 import distance_travelled_p1, distance_travelled_p2
    print("\nBENCHMARK DAY 12:")
    number = 100
    with open('inputs/i12.txt', 'r') as f:
        instrs = f.read().strip().split("\n")
        print(
            f"PART 1: Ran distance_travelled_p1() {number} times, average result: {do_timeit('distance_travelled_p1(instrs)', locals(), number)} seconds")
        print(
            f"PART 2: Ran distance_travelled_p2() {number} times, average result: {do_timeit('distance_travelled_p2(instrs)', locals(), number)} seconds")


d12()
