from commitHistory import Commit
import string_compare

#                                 branch sensitive?
#    include          [1. branch,contrib ] [3. !branch,contrib ]
#    contributors?    [2. branch,!contrib] [4. !branch,!contrib]
def code_review_ranking(id, commitHistory, string_compare_method=string_compare.LCP, scenario='scenario1'):
    all_reviewers = dict()
    commit_t = commitHistory.commitIDMap[id]  # target commit
    if scenario == 'scenario1' or scenario == 'scenario2':
        commits_p = commitHistory.get_commits_in_tree(id)  # all past commits set
    else:
        commits_p = commitHistory.get_previous_commits(id)  # all past commits by time set
    file_paths_t = commit_t.filePathsChanged  # file paths changed of target commits
    len_t = len(file_paths_t) # for normalization
    for id_p in commits_p:
        c = commitHistory.commitIDMap[id_p]
        file_paths_p = c.filePathsChanged  # set of past file path changed
        reviewers_p = c.reviewers  # set of past reviewers
        authors_p = c.authors  # set of past authors
        # put new mapping into dic if necessary
        for r in c.reviewers:
            if r not in all_reviewers:
                all_reviewers[r] = 0
        if scenario == 'scenario1' or scenario == 'scenario3':
            for a in c.authors:
                if a not in all_reviewers:
                    all_reviewers[a] = 0
        # calculate score and add to our mapping
        len_p = len(file_paths_p) # for normalization
        for file_path_p in file_paths_p:
            for file_path_t in file_paths_t:
                for r in reviewers_p:
                    all_reviewers[r] += string_compare_method(file_path_p, file_path_t) / (len_p * len_t)
                if scenario == 'scenario1' or scenario == 'scenario3':
                    for a in authors_p:
                        if a in all_reviewers:
                            all_reviewers[a] += string_compare_method(file_path_p, file_path_t) / (len_p * len_t)
    return all_reviewers
