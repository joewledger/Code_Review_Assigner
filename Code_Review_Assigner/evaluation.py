import code_review_ranking as crr
import parse_git_log as pgl
import string_compare as sc
import os


def calculate_average_ground_truth_position(repo_name, scenario="scenario3", string_compare_method=sc.LCP, limit=None):
    history = pgl.parse(os.getcwd() + "//" + repo_name + "//")
    commit_ids_with_reviewers = history.get_commit_ids_with_reviewers(limit)

    running_sum = 0
    for commit_id in commit_ids_with_reviewers:
        recommendations = sorted_recommendations(crr.code_review_ranking(
            commit_id, history, scenario=scenario, string_compare_method=string_compare_method))
        reviewer = list(history[commit_id].reviewers)[0]
        try:
            running_sum += recommendations.index(reviewer) + 1
        except:
            running_sum += len(recommendations) + 1

    return running_sum / len(commit_ids_with_reviewers)


def calculate_average_accuracy_for_sliding_window_k(repo_name, scenario="scenario3", string_compare_method=sc.LCP, k_values=range(1, 10), limit=None):
    history = pgl.parse(os.getcwd() + "//" + repo_name + "//")
    commit_ids_with_reviewers = history.get_commit_ids_with_reviewers(limit)

    accuracy_scores = {k: 0.0 for k in k_values}

    for commit_id in commit_ids_with_reviewers:
        recommendations = sorted_recommendations(crr.code_review_ranking(commit_id, history, scenario=scenario,
                                                                 string_compare_method=string_compare_method))
        reviewer = list(history[commit_id].reviewers)[0]

        for k in k_values:
            if(reviewer in recommendations[:k]):
                accuracy_scores[k] += 1

    return {k: accuracy_scores[k] / len(commit_ids_with_reviewers) for k in k_values}


def sorted_recommendations(recommendations):
    return sorted(recommendations.keys(), key=lambda x: recommendations[x], reverse=True)


if __name__ == "__main__":
    print(calculate_average_ground_truth_position("../help/", scenario="scenario1", limit=10))
    print(calculate_average_accuracy_for_sliding_window_k("../help/", scenario="scenario1", limit=10))
