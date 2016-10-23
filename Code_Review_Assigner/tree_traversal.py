from commitHistroy import *

def tree_traversal(commitHistory, commitID, tree):
	if commitHistory[commitID].parent is None:
		return tree
	for parent in commitHistory[commitID].parents:
		tree.add(parent.id)
		tree_traversal(commitHistory, commitHistory[parent.id].parents, tree)

def main():
   	tree = set()
   	tree_traversal(commitHistory, commitID, tree)

if __name__ == '__main__': main()
