from .commitHistory import Commit
from .string_compare import *

#                                 branch sensitive?
#    include          [1. branch,contrib ] [3. !branch,contrib ]
#    contributors?    [2. branch,!contrib] [4. !branch,!contrib]

# 1. Scenario 1:
# In this scenario, both branches and contributors are included.
def Scenario_1(id, commitHistory, method):
    all_reviewers = []
    commit_t = commitHistory.commitIDMap[id]              # target commit
    commits_p = commitHistory.get_commits_in_tree(id)   # all past commits set
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
                    r.score += string_compare(file_path_p, file_path_t, method)
                for a in authors_p:
                    a.score += string_compare(file_path_p, file_path_t, method)

# 2. Scenario 2:
# In this scenario, contributors are included.
def Scenario_2(id, commitHistory, method):
    all_reviewers = []
    commit_t = commitHistory.commitIDMap[id]              # target commit
    commits_p = commitHistory.get_commits_in_tree(id)   # all past commits by time set
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
                    r.score += string_compare(file_path_p, file_path_t, method)
                for a in authors_p:
                    a.score += string_compare(file_path_p, file_path_t, method)

# Scenario 3:
# In this scenario, branches are included.
def Scenario_3(id, commitHistory, method):
    all_reviewers = []
    commit_t = commitHistory.commitIDMap[id]              # target commit
    commits_p = commitHistory.get_previous_commits(id)   # all past commits set
    file_paths_t = commit_t.filePathsChanged     # file paths changed of target commits
    for c in commits_p:
        file_paths_p = c.filePathsChanged  # set of past file path changed
        reviewers_p = c.reviewers          # set of past reviewers
        all_reviewers.append(reviewers_p)
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    r.score += string_compare(file_path_p, file_path_t, method)



# Scenario 4:
# In this scenario, neither branches and contributors are included. Actually,
# this is the original work of RevFinder. Here, we only consider the past commits in master branch and the reviewers only.
def Scenario_4(id, commitHistory, method):
    all_reviewers = []
    commit_t = commitHistory.commitIDMap[id]              # target commit
    commits_p = commitHistory.get_previous_commits(id)   # all past commits by time set
    file_paths_t = commit_t.filePathsChanged     # file paths changed of target commits
    for c in commits_p:
        file_paths_p = c.filePathsChanged  # set of past file path changed
        reviewers_p = c.reviewers          # set of past reviewers
        all_reviewers.append(reviewers_p)
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    r.score += string_compare(file_path_p, file_path_t, method)

def code_review_ranking(id, commitHistory, **kwargs):
    method = kwargs.get('method')
    scenario = kwargs.get('scenario')
    all_reviewers = dict()
    commit_t = commitHistory.commitIDMap[id]  # target commit
    if scenario is 'scenario1' or 'scenario2':
        commits_p = commitHistory.get_commits_in_tree(id)  # all past commits set
    else:
        commits_p = commitHistory.get_previous_commits(id)  # all past commits by time set
    file_paths_t = commit_t.filePathsChanged  # file paths changed of target commits
    for c in commits_p:
        file_paths_p = c.filePathsChanged  # set of past file path changed

        reviewers_p = c.reviewers  # set of past reviewers
        authors_p = c.authors  # set of past authors

        # put new mapping into dic if necessary
        for r in c.reviewers:
            if r not in all_reviewers:
                all_reviewers[r] = 0
        if scenario is 'scenario1' or 'scenario3':
            for a in c.authors:
                if a not in all_reviewers:
                    all_reviewers[a] = 0
        # calculate score and add to our mapping
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    all_reviewers[r] += string_compare(file_path_p, file_path_t, method) # increment score
                if scenario is 'scenario1' or 'scenario3':
                    for a in authors_p:
                        if a in all_reviewers:
                            all_reviewers[a] += string_compare(file_path_p, file_path_t, method) # increment score
    return all_reviewers


