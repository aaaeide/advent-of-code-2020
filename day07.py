from typing import Dict, Set, List

example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

Graph = Dict[str, Dict[str, Set[str]]]


def create_graph(inp: str) -> Graph:
    """Graph represented as a dictionary of nodes where the key is the node ID (bag color), which 
       points to a dictionary {children: set(...outgoing edges), parents: set(...incoming edges)}.
    """
    graph: Graph = dict()

    def initialize_node(node_id: str, children: Set[str] = set(), parents: Set[str] = set()):
        nonlocal graph
        graph[node_id] = {
            'children': children, 'parents': parents}

    def add_node_from_rule(graph: Graph, rule: str):
        (node_id, children_str) = rule.split(" bags contain ")
        children = set()
        if children_str != "no other bags.":
            for bag_id_str in children_str.split(', '):
                children.add(" ".join(bag_id_str.split(" ")[1:-1]))

        # A single rule gives us every child of a given node...
        if node_id not in graph:
            initialize_node(node_id)
        graph[node_id]['children'] = children

        # ...and for each child it adds one known parent – the node.
        for child in children:
            if child not in graph:
                initialize_node(child,
                                parents=set([node_id]))
            else:
                graph[child]['parents'].add(node_id)

        return graph

    for rule in inp.split("\n"):
        graph = add_node_from_rule(graph, rule)

    return graph


def find_all_parents_bottomup_iter(graph: Graph, initial_node: str) -> Set[str]:
    fringe = set(graph[initial_node]['parents'])
    explored = set([initial_node])

    while len(fringe) != 0:
        nd = fringe.pop()
        unexplored_parents = {parent for parent in set(
            graph[nd]['parents']) if parent not in explored}
        fringe = fringe.union(unexplored_parents)
        explored.add(nd)

    explored -= set([initial_node])
    return explored


def find_all_parents_bottomup_rec(graph: Graph, initial_node: str) -> Set[str]:
    # The nodes we end up visiting are the parents of the input node
    visited: Set[str] = set()
    initial_fringe = set(graph[initial_node]['parents'])

    def explore(visited: Set[str], node: str) -> None:
        visited.add(node)
        for nd in graph[node]['parents']:
            if nd not in visited:
                explore(visited, nd)

    for nd in initial_fringe:
        if nd not in visited:
            explore(visited, nd)

    return visited


def find_all_parents_topdown(graph: Graph, goal_nd: str) -> Set[str]:
    parents: Set[str] = set()
    yet_to_check = set(graph.keys())

    def check_parenthood(nd: str):
        nonlocal parents, yet_to_check
        # Memoization
        if nd not in yet_to_check:
            if nd in parents:
                return True
            return False

        # Base case 1: No children
        if len(graph[nd]['children']) == 0:
            yet_to_check.remove(nd)
            return False

        # Base case 2: Found goal node
        if goal_nd in graph[nd]['children']:
            print("FOUND GOAL DIRECTLY!")
            yet_to_check.remove(nd)
            parents.add(nd)
            return True

        return any([check_parenthood(child) for child in graph[nd]['children']])

    while len(yet_to_check) != 0:
        nd = yet_to_check.pop()
        check_parenthood(nd)

    return parents


def part1(inp: str):
    graph = create_graph(inp)
    parents_rec = find_all_parents_bottomup_rec(graph, 'shiny gold')
    parents_iter = find_all_parents_bottomup_iter(graph, 'shiny gold')

    print("\tbottom up attempts:")
    print("\t\trecursively", len(parents_rec))
    print("\t\titeratively", len(parents_iter))

    parents_rec = find_all_parents_topdown(graph, 'shiny gold')

    print("\ttop down attempts:")
    print("\t\trecursively", len(parents_rec))


with open('inputs/i07.txt', 'r') as f:
    inp = f.read().strip()
    print(f"EXAMPLE:")
    part1(example)

    # print(f"\nPART 1:")  # 555 too high
    # part1(inp)
