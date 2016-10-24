from collections import *


class commitHistory(object):
    """description of class"""

    def __init__(self):
        # Commits are ordered by their timestamp
        self.commitIDMap = OrderedDict()

    # Gets all previous commits (as indicated by the commits timestamp).
    def get_previous_commits(self, commit_id):
        idx = list(self.commitIDMap).index(commit_id)
        return set(list(self.commitIDMap)[0:idx])


    # Gets all previous commits by parent relationship to origin
    def get_commits_in_tree(self, commitID, tree=set()):
        for parent in self.commitIDMap[commitID].parents:
            tree.add(parent)
            tree = self.get_commits_in_tree(parent, tree)
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
