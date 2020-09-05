# class Tree:
#     def __init__(self, limit, depth):
#         self.root = Node("root")
#         Tree.make_tree(self.root, limit, depth)
#
#     @staticmethod
#     def make_tree(parent, limit, depth):
#         for i in range(limit):
#             child = Node((depth, i))
#             parent.add_child(child)
#             if depth:
#                 Tree.make_tree(child, limit+1, depth-1)
#         # return parent
#
#     def printer(self):
#         print()
#         self.root.printer()
#
#
# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []
#         self.parent = None
#
#     def add_child(self, child):
#         self.children.append(child)
#         # child.parent = self
#
#     def printer(self, counter=0):
#         print(counter*'\t', self.name)
#         for child in self.children:
#             child.printer(counter+1)
#
#
# tree = Tree(3, 3)
# tree.printer()


from anytree import NodeMixin, RenderTree, Node
from anytree.walker import Walker


class Cell(NodeMixin):
    def __init__(self, name, parent=None, children=None):
        super().__init__()
        self.name = name
        self.parent = parent
        if children:
            self.children = children

    # def __str__(self):
    #     return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


def make_tree2(parent, limit, depth, level=0):
    for i in range(limit, limit+3):
        child = Cell((depth, i), parent=parent)
        if depth:
            make_tree2(child, limit+i*3, depth-1, level+2)
            # make_tree(child, limit, depth-1)


root2 = Cell("root")
make_tree2(root2, 3, 4)
#
# for i in range(3):
#     kwargs = {"lol": i+1}
#     node_1 = Cell((i,), parent=root2)
#     for j in range(3):
#         kwargs2 = {"lol": (i*j+1)**2}
#         node_2 = Cell((i, j), parent=node_1)


for pre, _, node in RenderTree(root2):
    print(f"{pre}{node.name}")

# w = Walker()
# print(w.walk(root2, node_2))
#
# print(node_2)


from anytree.exporter import DotExporter
from graphviz import render


filename = "my_tree_lol.gv"

DotExporter(root2).to_picture(filename)

render("dot", "pdf", filename)

# (
#     (
#         Node('/f/g/i/h'),
#         Node('/f/g/i'),
#         Node('/f/g')
#     ),
#     Node('/f'),
#     (
#         Node('/f/b'),
#         Node('/f/b/d'),
#         Node('/f/b/d/e')
#     )
# )

