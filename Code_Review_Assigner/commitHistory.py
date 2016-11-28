from collections import *
from queue import Queue

import parse_git_log as pgl

class commitHistory(object):
    """description of class"""

    def __init__(self, folderPath):
        # Commits are ordered by their timestamp
        self.commitIDMap = OrderedDict()
        self.folderPath = folderPath

    # Gets all previous commits (as indicated by the commits timestamp).
    def get_previous_commits(self, commit_id):
        idx = list(self.commitIDMap).index(commit_id)
        return set(list(self.commitIDMap)[0:idx])


    # Gets all previous commits by parent relationship to origin
    def get_commits_in_tree(self, commitID):
        return pgl.revlist(self.folderPath, commitID)

    def get_commit_ids_with_reviewers(self):
        return [x for x in self.commitIDMap if len(self.commitIDMap[x].reviewers) > 0]


    def __getitem__(self, id):
        return self.commitIDMap[id]

    def __str__(self):
        return "Commit history with %d commits" % len(self.commitIDMap)


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
