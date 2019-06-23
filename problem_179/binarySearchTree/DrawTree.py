from math import ceil, floor
from collections import defaultdict


class DrawTree():
    def __init__(self, tree, depth=0):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(t, depth + 1) for t in tree]
        self.mod = 0


def layout(tree):
    setup(tree)
    addmods(tree)
    return tree


def setup(tree, depth=0, nexts=None, offset=None):
    if tree is None:
        return

    if nexts is None:
        nexts = defaultdict(lambda: 0)
    if offset is None:
        offset = defaultdict(lambda: 0)

    for c in tree.children:
        setup(c, depth+1, nexts, offset)

    tree.y = depth

    if not tree.children:
        place = nexts[depth]
        tree.x = place
    elif len(tree.children) == 1:
        place = tree.children[0].x - 1
    else:
        s = tree.children[0].x + tree.children[1].x
        place = s / 2

    offset[depth] = max(offset[depth], nexts[depth]-place)

    if tree.children:
        tree.x = place + offset[depth]

    nexts[depth] += 4
    tree.mod = offset[depth]


def addmods(tree, modsum=0):
    tree.x = tree.x + modsum
    modsum += tree.mod

    for t in tree.children:
        addmods(t, modsum)


def printTree(drawTree, lines=None, depth=0):
    if not lines:
        lines = defaultdict(lambda: [])

    line = lines[depth]
    if len(line) <= drawTree.x:
        line.extend([' '] * ceil(drawTree.x - (len(line) - 1)))

    line[floor(drawTree.x)] = str(drawTree.tree.value)

    for c in drawTree.children:
        printTree(c, lines, depth+1)

    sortedKeys = list(lines.keys())
    sortedKeys.sort()
    return [lines[v] for v in sortedKeys]
