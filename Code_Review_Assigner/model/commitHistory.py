class commitHistory(object):
    """description of class"""

    def __init__(self):
        self.commitIDMap = {}
  

class commit(object):
    """description of class"""

    def __init__(self, commitID):
        self.commitID = commitID
        self.authors = set()
        self.reviewers = set()
        self.filePathsChanged = set()
        self.previousCommit = set() #set for merge commits

    def getPreviousCommitsInBranch():
        return set() #recursive