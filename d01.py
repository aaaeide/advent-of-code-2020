def find_2sum(arr, target):
    for a in {s for s in arr if s < target}:
        for b in {s for s in arr if s == target - a}:
            return a * b


def find_3sum(arr, target):
    for a in {s for s in arr if s < target}:
        for b in {s for s in arr if s < target-a}:
            for c in {s for s in arr if s == target-a-b}:
                return a*b*c


def part1():
    with open('i01.txt', 'r') as inp:
        int_inp = [int(i_str) for i_str in inp.readlines()]
        sol = find_2sum(int_inp, 2020)
    return sol


def part2():
    with open('i01.txt', 'r') as inp:
        int_inp = [int(i_str) for i_str in inp]
        sol = find_3sum(int_inp, 2020)
    return sol


if __name__ == '__main__':
    print("PART 1:", part1())
    print("PART 2:", part2())
