<<<<<<< HEAD
from collections import *

class commitHistory(object):
    """description of class"""

    def __init__(self):
        #Commits are ordered by their timestamp
        self.commitIDMap = OrderedDict()

    #Gets all previous commits (as indicated by the commits timestamp). 
    #If branch_id is specified, only commits that are part of that branch are included
    def get_previous_commits(commit_id, branch_id=None):
        return None


=======
class CommitHistory(object):
    """description of class"""

    def __init__(self):
        self.commitIDMap = {}
>>>>>>> f1de8c6ab4f00310b32ada71921ae65e9028c12e


class Commit(object):
    """description of class"""

    def __init__(self, commitID):
        self.commitID = commitID
        self.timestamp = None
        self.authors = set()
        self.reviewers = set()
        self.filePathsChanged = set()
<<<<<<< HEAD
        self.branches_included_in = set() #set of all branches the given commit is a part of

    def getPreviousCommitsInBranch():
        return set() #recursive
=======
        self.previousCommit = set()  # set for merge commits

    def getPreviousCommitsInBranch():
        return set()  # recursive


class Reviewer:
    def __init__(self):
        self.score = 0
>>>>>>> f1de8c6ab4f00310b32ada71921ae65e9028c12e
