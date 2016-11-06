from collections import *
import queue.Queue

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
        current_commits = Queue()
        current_commits.put(self.commitIDMap[commitID])

        while(not current_commits.empty()):
            commit = current_commits.get()
            for parent in commit.parents:
                tree.add(parent)
                current_commits.put(self.commitIDMap[parent])

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
