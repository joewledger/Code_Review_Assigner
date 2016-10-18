from ..model.commitHistory import *

#                                 branch sensitive?
#    include          [1. branch,contrib ] [3. !branch,contrib ]
#    contributors?    [2. !branch,contrib] [4. !branch,!contrib]

# 1. trace current branch to origin
#    include contributors/author for weighting
c = commit
cps = commit.getPreviousCommitsInBranch()
for cp in cp:


# 2. use all previous commits
#    include contributors/author for weighting

# 3. trace current branch to origin
#    exclude contributors/author for weighting

# 4. use all previous commits
#    exclude contributors/author for weighting
