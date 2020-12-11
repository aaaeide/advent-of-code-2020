from typing import Dict, List, Tuple, Union


ex = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip().split("\n")


def get_next_here_adj(map: List[str], x: int, y: int) -> str:
    here = map[y][x]
    if here == '.':
        return here

    adj_occ = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) != (x, y) and 0 <= i < len(map[0]) and 0 <= j < len(map):
                if map[j][i] == '#':
                    if here == 'L':
                        return 'L'
                    # here = '#'
                    adj_occ += 1
                    if adj_occ == 4:
                        return 'L'
    if here == 'L':
        return '#'
    return here


def get_next_here_sight(map: List[str], x: int, y: int) -> str:
    here = map[y][x]
    HEIGHT = len(map)
    WIDTH = len(map[0])
    if here == '.':
        return here

    sight: Dict[Tuple[int, int], Union[None, str]] = {
        (-1, -1):   None,
        (0, -1):    None,
        (1, -1):    None,
        (-1, 0):    None,
        # ignore chair itself
        (1, 0):     None,
        (-1, 1):    None,
        (0, 1):     None,
        (1, 1):     None,
    }
    layer = 1   # think like an onion
    while None in sight.values():
        for (xsign, ysign) in filter(lambda signs: sight[signs] == None, sight):
            x_cur, y_cur = x + xsign*layer, y + ysign*layer
            # edge detection
            if not (0 <= x_cur < WIDTH and 0 <= y_cur < HEIGHT):
                # we are still at None in this direction and are outside the map
                sight[(xsign, ysign)] = '.'
                continue
            can_see = map[y_cur][x_cur]
            sight[(xsign, ysign)] = can_see if can_see != '.' else None
        layer += 1

    if here == 'L' and list(sight.values()).count("#") == 0:
        return '#'
    if here == '#' and list(sight.values()).count("#") >= 5:
        return 'L'
    return here


def get_next_state(map: List[str], part=1) -> List[str]:
    next = []
    for y in range(len(map)):
        next_line = ''
        for x in range(len(map[y])):
            if part == 1:
                next_line += get_next_here_adj(map, x, y)
            else:
                next_line += get_next_here_sight(map, x, y)
        next.append(next_line)
    return next


def find_stable_state(map: List[str], part=1, verbose=False) -> List[str]:
    i = 0
    while True:
        i += 1
        nxt = get_next_state(map, part=part)
        if verbose:
            print("\n".join(nxt))
            input("continue?")
        if nxt == map:
            return map
        map = nxt


def solve(inp: List[str], part=1):
    return sum([sum([1 for pos in line if pos == '#']) for line in find_stable_state(inp, part=part)])


if __name__ == '__main__':
    print("EX P1:\t", solve(ex))
    with open('inputs/i11.txt', 'r') as f:
        map = f.read().strip().split("\n")
        print("P1:\t", solve(map))
        print("P2:\t", solve(map, 2))
