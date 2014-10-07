import random

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.length = 0

    def add(self, newval):
        temp = self
        inserted = False
        while not inserted:
            if newval < temp.val:
                if temp.left is None:
                    temp.left = Tree(newval)
                    inserted = True
                else:
                    temp = temp.left
            elif newval > temp.val:
                if temp.right is None:
                    temp.right = Tree(newval)
                    inserted = True
                else:
                    temp = temp.right
            else:
                return False
        self.length += 1
        return True
    
    def printTree(self, depth=1):
        print "depth: " + str(depth) + ", val: " + str(self.val)
        if self.left is not None:
            self.left.printTree(depth + 1)
        if self.right is not None:
            self.right.printTree(depth + 1)

def sum_paths_from_root(tree, num):
    if tree == None or tree.val > num:
        return []
    if tree.val == num:
        return [tree.val]
    retlist = []
    left = sum_paths_from_root(tree.left, num - tree.val)
    right = sum_paths_from_root(tree.right, num - tree.val)
    if left:
        if isinstance(left[0], list):
            left = [item for sublist in left for item in sublist]
        left.append(tree.val)
        retlist.append(left)
    if right:
        if isinstance(right[0], list):
            right = [item for sublist in right for item in sublist]
        right.append(tree.val)
        retlist.append(right)
    return retlist

def get_sum_paths(tree, num):
    if tree == None or tree.val > num:
        return
    path = sum_paths_from_root(tree, num)
    if path:
        print path
    get_sum_paths(tree.left, num)
    get_sum_paths(tree.right, num)

limit = 10
tree = Tree(random.randint(0, limit))

while tree.length < limit:
    tree.add(random.randint(0, limit))

tree.printTree()
get_sum_paths(tree, limit)
# print sum_paths_from_root(tree.right, limit)
