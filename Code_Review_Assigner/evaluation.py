import code_review_ranking as crr
import parse_git_log as pgl

def calculate_average_ground_truth_position(repo_name, recommendation_method="", string_compare_method=""):
	return None


def calculate_average_accuracy_for_sliding_window_k(repo_name, recommendation_method = "", string_compare_method="", k_values=list(range(0,10))):
	return None


if __name__ == "__main__":
	history = pgl.parse('../help/')
	commit_id = history.get_last_commit()
	print(commit_id)
	print(crr.code_review_ranking(commit_id, history))