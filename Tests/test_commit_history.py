import os
import Code_Review_Assigner.parse_git_log as pgl
import Code_Review_Assigner.commitHistory as ch


def test_commit_history(dirPath=os.getcwd()):
    myCommitHistory = pgl.parse(dirPath)

    # https://github.com/joewledger/Code_Review_Assigner/commit/61206b44a3511c3252a130144cf3ddaa3ae93029
    commitID = 'f8d4bc0cf7cf7f1ccf1525660f2212edae3c8972'
    
    tree = myCommitHistory.get_commits_in_tree(commitID)

    prev = myCommitHistory.get_previous_commits(commitID)
    print(len(prev))
