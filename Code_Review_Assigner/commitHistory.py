from collections import *


class commitHistory(object):
    """description of class"""

    def __init__(self):
        # Commits are ordered by their timestamp
        self.commitIDMap = OrderedDict()

    # Gets all previous commits (as indicated by the commits timestamp).
    # If branch_id is specified, only commits that are part of that branch are included
    def get_previous_commits(commit_id, branch_id=None):
        #branch_id = None all

        return None

    def tree_traversal(self, commitID, tree=set()):
        for parent in self.commitIDMap[commitID].parents:
            tree.add(parent)
            tree = self.tree_traversal(parent, tree)
        return tree

class Commit(object):
    """description of class"""

    def __init__(self, id):
        self.id = id
        self.timestamp = None
        self.authors = set()
        self.reviewers = set()
        self.filePathsChanged = set()
        self.parents = set()
        self.branches_included_in = set()  # set of all branches the given commit is a part of


class Reviewer:
    def __init__(self):
        self.score = 0
