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


d01()
d02()
d03()
d04()
d05()
