import os
from parse_git_log import *
from commitHistory import *

def main(dirPath=os.getcwd()):
    myCommitHistory = parse(dirPath)

    # https://github.com/joewledger/Code_Review_Assigner/commit/61206b44a3511c3252a130144cf3ddaa3ae93029
    commitID = 'f8d4bc0cf7cf7f1ccf1525660f2212edae3c8972'
    
    tree = myCommitHistory.get_commits_in_tree(commitID)

    prev = myCommitHistory.get_previous_commits(commitID)
    print(len(prev))

if __name__ == '__main__': 
    main()