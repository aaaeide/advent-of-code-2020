from typing import Dict, Tuple

Dag = Dict[str, Dict[str, int]]


def create_dag(inp: str) -> Dag:
    def parse_rule(rule: str) -> Tuple[str, Dict[str, int]]:
        (node_id, children_str) = rule.strip().split(" bags contain ")
        children: Dict[str, int] = {}
        if children_str != 'no other bags.':
            for child_str in children_str.strip().split(', '):
                child_splt = child_str.split(" ")
                number = int(child_splt[0])
                child = " ".join(child_str.split(" ")[1:-1])
                children[child] = number

        return (node_id, children)

    dag: Dag = dict()
    for line in inp.strip().split("\n"):
        (node, children) = parse_rule(line)
        dag[node] = children

    return dag


def find_num_parents(dag: Dag, goal: str) -> int:
    def find_node(dag: Dag, start: str, goal: str) -> bool:
        children = dag[start]

        if goal in children:
            return True
        if len(children) == 0:
            return False

        for child in children:
            if find_node(dag, child, goal):
                return True
        return False

    parents_found = 0
    for node in dag:
        if find_node(dag, node, goal):
            parents_found += 1

    return parents_found


def find_total_num_bags(dag: Dag, start: str) -> int:
    children = dag[start]
    total_bags = 1  # the bag itself

    for child in children:
        total_bags += children[child] * find_total_num_bags(dag, child)

    return total_bags


def part1(inp: str):
    dag = create_dag(inp)
    return find_num_parents(dag, 'shiny gold')


def part2(inp: str):
    dag = create_dag(inp)
    return find_total_num_bags(dag, 'shiny gold') - 1


if __name__ == '__main__':
    with open('inputs/i07.txt', 'r') as f:
        inp = f.read()
        print("PART 1", part1(inp))
        print("PART 2", part2(inp))
