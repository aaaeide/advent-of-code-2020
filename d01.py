def find_2sum(arr, target):
    looking_for = set()
    for el in arr:
        if el in looking_for:
            return el * (target-el)
        looking_for.add(target-el)


def find_3sum(arr, target):
    for a in {s for s in arr if s < target}:
        for b in {s for s in arr if s < target-a}:
            for c in {s for s in arr if s == target-a-b}:
                return a*b*c


# example = [1721, 979, 366, 299, 675, 1456]
# print(find_2sum(example, 2020))
# print(find_3sum(example, 2020))


with open('i01.txt', 'r') as inp:
    int_inp = [int(i_str) for i_str in inp]
    sol_p1 = find_2sum(int_inp, 2020)
    sol_p2 = find_3sum(int_inp, 2020)
    print(f"PART 1:\t{sol_p1}")
    print(f"PART 2:\t{sol_p2}")
