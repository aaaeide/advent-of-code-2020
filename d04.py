import re
from functools import reduce

req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid_keysets = (req_fields, {*req_fields, "cid"})

rules = {
    "byr": lambda byr: re.match(r"^\d{4}$", byr) != None and 1920 <= int(byr) <= 2002,
    "iyr": lambda iyr: re.match(r"^\d{4}$", iyr) != None and 2010 <= int(iyr) <= 2020,
    "eyr": lambda eyr: re.match(r"^\d{4}$", eyr) != None and 2020 <= int(eyr) <= 2030,
    "hgt": lambda hgt: re.match(r"^(1[5-8][0-9]cm)|(19[0-3]cm)|59in|(6[0-9]in)|(7[0-6]in)$", hgt) != None,
    "hcl": lambda hcl: re.match(r"^#[0-9a-fA-F]{6}$", hcl) != None,
    "ecl": lambda ecl: ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda pid: re.match(r"^\d{9}$", pid) != None,
    "cid": lambda _: True
}


def parse_and_count_valid(inp: str):
    ct1 = 0
    ct2 = 0
    for entry in [re.sub(r"\s", " ", line) for line in inp.split("\n\n")]:
        kv = [tuple(kv.split(":")) for kv in entry.strip().split(" ")]
        keys = {pair[0] for pair in kv if pair[0] != ''}
        if keys in valid_keysets:
            ct1 += 1
            if reduce(lambda x, y: x and y,
                      [rules[key](val) for (key, val) in kv]):
                ct2 += 1
    return ct1, ct2


if __name__ == '__main__':
    with open('inputs/i04.txt', 'r') as f:
        res = parse_and_count_valid(f.read())
        print(f"PART 1: {res[0]} valid passports")
        print(f"PART 2: {res[1]} valid passports")
        print(rules["byr"]("200a"))
