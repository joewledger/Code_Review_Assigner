import os
from parse_git_log import *
from commitHistory import *

def main(dirPath=os.getcwd()):
    myCommitHistory = parse(dirPath)

    # https://github.com/joewledger/Code_Review_Assigner/commit/61206b44a3511c3252a130144cf3ddaa3ae93029
    commitID = '61206b44a3511c3252a130144cf3ddaa3ae93029'
    
    tree = myCommitHistory.tree_traversal(commitID)
    print(len(tree))

if __name__ == '__main__': 
    main()