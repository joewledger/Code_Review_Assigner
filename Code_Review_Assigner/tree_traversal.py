def tree_traversal(IDmap, commitID, tree):
    for parent in IDmap[commitID].parents:
        tree.add(parent)
        tree = tree_traversal(IDmap, parent, tree)
    return tree