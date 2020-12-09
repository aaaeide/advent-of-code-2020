from typing import Tuple, List


ex = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
Program = List[Tuple[str, int]]


def parse_program(inp: str) -> Program:
    return [(op, int(arg)) for (op, arg) in [instr.split(" ") for instr in inp.split("\n")]]


def run_program(program: Program) -> Tuple[int, int]:
    history = []
    acc = 0
    pc = 0
    err = 0

    while pc < len(program):
        if pc in history:  # err
            err = 1
            break

        history.append(pc)
        (op, arg) = program[pc]

        if op == 'acc':
            acc += arg
        if op == 'jmp':
            pc += arg-1

        pc += 1
    return (err, acc)


def fix_program(program: Program) -> int:
    i = 0
    while i < len(program):
        (op, arg) = program[i]
        new_program = program.copy()
        if op == 'jmp':
            new_program[i] = ('nop', arg)
        elif op == 'nop':
            new_program[i] = ('jmp', arg)
        else:
            i += 1
            continue

        res = run_program(new_program)
        if res[0] == 0:
            return res[1]

        i += 1

    print("Program unfixable")
    return -1


def part1(inp: str):
    program = parse_program(inp)
    return run_program(program)[1]


def part2(inp: str):
    program = parse_program(inp)
    return fix_program(program)


if __name__ == '__main__':
    with open('inputs/i08.txt', 'r') as f:
        inp = f.read().strip()
        program = parse_program(inp)
        print("PART 1", run_program(program)[1])
        print("PART 2", fix_program(program))
