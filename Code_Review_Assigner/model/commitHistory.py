class commitHistory(object):
    """description of class"""

    def __init__(self):
        self.commitIDMap = {}


class commit(object):
    """description of class"""

    def __init__(self, commitID):
        self.commitID = commitID
        self.timestamp = None
        self.authors = set()
        self.reviewers = set()
        self.filePathsChanged = set()
        self.branches_included_in = set() #set of all branches the given commit is a part of

    def getPreviousCommitsInBranch():
        return set() #recursive
