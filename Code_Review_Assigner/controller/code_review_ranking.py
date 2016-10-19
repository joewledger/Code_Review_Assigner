from ..model.commitHistory import *
from .string_compare import *

#                                 branch sensitive?
#    include          [1. branch,contrib ] [3. !branch,contrib ]
#    contributors?    [2. !branch,contrib] [4. !branch,!contrib]

# 1. trace current branch to origin
#    include contributors/author for weighting


# 2. use all previous commits
#    include contributors/author for weighting

# 3. trace current branch to origin
#    exclude contributors/author for weighting

# 4. use all previous commits
#    exclude contributors/author for weighting
commit = Commit
target_file_paths = commit.filePathsChanged
past_commits = commit.get_previous_commits(commit.commitID)
reviewers = set()
for target_file_path in target_file_paths:  # for each paths in commit
    for past_commit in past_commits:  # check all the past commits
        paths_changed = past_commit.filePathsChanged
        commit_reviewers = past_commit.reviewers
        for path in paths_changed:  # for each review's reviewed file path
            score = string_alignment(target_file_path, path)
            for commit_reviewer in commit_reviewers:
                commit_reviewer.score += score