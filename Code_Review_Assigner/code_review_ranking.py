from .commitHistory import Commit
from .string_compare import *

#                                 branch sensitive?
#    include          [1. branch,contrib ] [3. !branch,contrib ]
#    contributors?    [2. !branch,contrib] [4. !branch,!contrib]

# 1. Scenario 1:
# In this scenario, both branches and contributors are included.
def Scenario_1:
    id = 'xxx'
    all_reviewers = []
    commit_t = Commit(id)              # target commit
    commits_p = get_commits_in_tree()   # all past commits set
    file_paths_t = commit_t.filePathsChanged     # file paths changed of target commits
    for c in commits_p:
        file_paths_p = c.filePathsChanged  # set of past file path changed
        reviewers_p = c.reviewers          # set of past reviewers
        authors_p = c.authors            # set of past authors
        all_reviewers.append(reviewers_p)
        all_reviewers.append(authors_p)
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    r.score += string_compare(file_path_p, file_path_t, method='def your method')
                for a in authors_p:
                    a.score += string_compare(file_path_p, file_path_t, method='def your method')

# 2. Scenario 2:
# In this scenario, contributors are included.
def Scenario_2:
    id = 'xxx'
    all_reviewers = []
    commit_t = Commit(id)              # target commit
    commits_p = get_commits_in_tree()   # all past commits by time set
    file_paths_t = commit_t.filePathsChanged     # file paths changed of target commits
    for c in commits_p:
        file_paths_p = c.filePathsChanged  # set of past file path changed
        reviewers_p = c.reviewers          # set of past reviewers
        authors_p = c.authors            # set of past authors
        all_reviewers.append(reviewers_p)
        all_reviewers.append(authors_p)
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    r.score += string_compare(file_path_p, file_path_t, method='def your method')
                for a in authors_p:
                    a.score += string_compare(file_path_p, file_path_t, method='def your method')

# Scenario 3:
# In this scenario, branches are included.
def Scenario_3:
    id = 'xxx'
    all_reviewers = []
    commit_t = Commit(id)              # target commit
    commits_p = get_commits_in_tree()   # all past commits set
    file_paths_t = commit_t.filePathsChanged     # file paths changed of target commits
    for c in commits_p:
        file_paths_p = c.filePathsChanged  # set of past file path changed
        reviewers_p = c.reviewers          # set of past reviewers
        all_reviewers.append(reviewers_p)
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    r.score += string_compare(file_path_p, file_path_t, method='def your method')



# Scenario 4:
# In this scenario, neither branches and contributors are included. Actually,
# this is the original work of RevFinder. Here, we only consider the past commits in master branch and the reviewers only.
def Scenario_4:
    id = 'xxx'
    all_reviewers = []
    commit_t = Commit(id)              # target commit
    commits_p = get_commits_in_tree()   # all past commits by time set
    file_paths_t = commit_t.filePathsChanged     # file paths changed of target commits
    for c in commits_p:
        file_paths_p = c.filePathsChanged  # set of past file path changed
        reviewers_p = c.reviewers          # set of past reviewers
        all_reviewers.append(reviewers_p)
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    r.score += string_compare(file_path_p, file_path_t, method='def your method')
