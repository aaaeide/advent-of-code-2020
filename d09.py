from typing import List


ex = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102,
      117, 150, 182, 127, 219, 299, 277, 309, 576]


def find_weird_num(preamble: int, numbers: List[int]) -> int:
    def check_weirdness(preamble: int, i: int, numbers: List[int]) -> bool:
        for j in range(i-preamble, i):
            for k in range(i-preamble, i):
                if j != k and numbers[j] + numbers[k] == numbers[i]:
                    return False
        return True

    for i in range(preamble, len(numbers)):
        if check_weirdness(preamble, i, numbers):
            return numbers[i]
    print("NO WEIRD NUMBER FOUND")
    return -1


def find_weird_sum(weird_num: int, numbers: List[int]) -> int:
    for i in range(len(numbers)):
        j = 1
        seq = [numbers[i], numbers[i+j]]
        while sum(seq) < weird_num:
            j += 1
            seq.append(numbers[i+j])
        if sum(seq) == weird_num:
            return min(seq) + max(seq)
    print("NO WEIRD SEQUENCE FOUND")
    return -1


if __name__ == "__main__":
    weird_num = find_weird_num(5, ex)
    weird_sum = find_weird_sum(weird_num, ex)
    print("EX P1:\t", weird_num)
    print("EX P2:\t", weird_sum)

    with open('inputs/i09.txt', 'r') as f:
        numbers = [int(line) for line in f.readlines()]
        weird_num = find_weird_num(25, numbers)
        weird_sum = find_weird_sum(weird_num, numbers)
        print("PART 1:\t", weird_num)
        print("PART 2:\t", weird_sum)
