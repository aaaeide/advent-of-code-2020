from typing import Tuple, List


def determine(tup, code):
    for half in code:
        (lower, upper) = tup
        if half in ("B", "R"):
            tup = (lower + (upper-lower)//2 + 1, upper)
        else:
            tup = (lower, lower + (upper-lower)//2)
    return tup[0]


def determine_seat_id(code: str) -> int:
    row = determine((0, 127), code[:7])
    col = determine((0, 7), code[7:])
    return row*8 + col


def determine_all_seat_ids(codes: List[str]) -> List[int]:
    return [determine_seat_id(code) for code in codes]


def max_seat_id(codes: List[str]) -> int:
    # Part 1
    return max(determine_all_seat_ids(codes))


def find_seat(codes: List[str]) -> int:
    ids = set(determine_all_seat_ids(codes))
    seatspace = set(range(min(ids), max(ids)+1))
    missing_seats_in_middle = seatspace - ids
    return missing_seats_in_middle.pop()


if __name__ == '__main__':
    with open('inputs/i05.txt', 'r') as f:
        codes = [line.strip() for line in f.readlines()]
        print(f"PART 1: {max_seat_id(codes)}")
        print(f"PART 2: {find_seat(codes)}")
