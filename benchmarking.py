import timeit


def d01():
    from d01 import part1 as d01p1, part2 as d01p2
    print("\nBENCHMARK DAY 01:")
    number = 100
    print(
        f"Ran part1() {number} times, average result: { timeit.timeit('d01p1()', globals=locals(), number=number)/number} seconds")
    print(
        f"Ran part2() {number} times, average result: {timeit.timeit('d01p2()', globals=locals(), number=number)/number} seconds")


def d02():
    from d02 import part1 as d02p1, part2 as d02p2
    print("\nBENCHMARK DAY 01:")
    number = 100
    print(
        f"Ran part1() {number} times, average result: { timeit.timeit('d02p1()', globals=locals(), number=number)/number} seconds")
    print(
        f"Ran part2() {number} times, average result: {timeit.timeit('d02p2()', globals=locals(), number=number)/number} seconds")


def d03():
    from d03 import part1 as d03p1, part2 as d03p2
    print("\nBENCHMARK DAY 03:")
    number = 100
    print(
        f"Ran part1() {number} times, average result: { timeit.timeit('d03p1()', globals=locals(), number=number)/number} seconds")
    print(
        f"Ran part2() {number} times, average result: {timeit.timeit('d03p2()', globals=locals(), number=number)/number} seconds")


d01()
d02()
d03()
