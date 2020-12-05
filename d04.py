import re
from functools import reduce

example = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

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
        print(f"EXAMPLE: {parse_and_count_valid(example)} valid passports")
        res = parse_and_count_valid(f.read())
        print(f"PART 1: {res[0]} valid passports")
        print(f"PART 2: {res[1]} valid passports")
        print(rules["byr"]("200a"))
