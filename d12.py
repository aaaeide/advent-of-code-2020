from typing import List, Tuple


ex = """
F10
N3
F7
R90
F11
""".strip().split("\n")


def travel(dir: str, amt: int) -> Tuple[int, int]:
    if dir == 'N':
        return (0, amt)
    if dir == 'E':
        return (amt, 0)
    if dir == 'S':
        return (0, -amt)
    return (-amt, 0)


def turn(facing: str, dir: str, deg: int) -> str:
    compass = 'N', 'E', 'S', 'W'
    sign = -1 if dir == 'L' else 1
    return compass[(compass.index(facing) + sign*(int(deg / 90))) % 4]


def rotate_waypoint(cur: Tuple[int, int], dir: str, deg: int) -> Tuple[int, int]:
    x, y = cur
    if dir == 'L':
        return [(-y, x), (-x, -y), (y, -x)][int(deg/90)-1]
    return [(y, -x), (-x, -y), (-y, x)][int(deg/90)-1]


def distance_travelled_p1(instrs: List[str]) -> int:
    facing = "E"
    travelled = (0, 0)  # (x,y)
    for instr in instrs:
        cmd, amt = instr[0], int(instr[1:])
        if cmd in ('L', 'R'):
            facing = turn(facing, cmd, amt)
            continue

        if cmd == "F":
            delta = travel(facing, amt)
        else:
            delta = travel(cmd, amt)
        travelled = (travelled[0] + delta[0], travelled[1] + delta[1])
    return abs(travelled[0]) + abs(travelled[1])


def distance_travelled_p2(instrs: List[str]) -> int:
    waypoint = (10, 1)
    ship_pos = (0, 0)
    for instr in instrs:
        cmd, amt = instr[0], int(instr[1:])
        if cmd in ('L', 'R'):
            waypoint = rotate_waypoint(waypoint, cmd, amt)
            continue

        x, y = waypoint

        if cmd == 'F':
            ship_pos = (ship_pos[0] + x*amt,
                        ship_pos[1] + y*amt)
            continue

        delta = travel(cmd, amt)
        waypoint = (waypoint[0] + delta[0], waypoint[1] + delta[1])
    return abs(ship_pos[0]) + abs(ship_pos[1])


if __name__ == '__main__':
    with open('inputs/i12.txt', 'r') as f:
        instrs = f.read().strip().split("\n")
        print("PART 1:\t", distance_travelled_p1(instrs))
        print("PART 2:\t", distance_travelled_p2(instrs))
