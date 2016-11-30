import matplotlib.pyplot as plt
import numpy as np
import evaluation


def plot_average_position(repo_name, limit=None):
    scenarios = ["scenario%d" % d for d in range(1, 5)]

    fig, axes = plt.subplots()

    ind = np.arange(len(scenarios))
    width = 0.35

    values = [evaluation.calculate_average_ground_truth_position(repo_name, scenario=s, limit=limit) for s in scenarios]

    axes.bar(ind + width / 2, values, width)
    axes.set_title("Average ranking of ground truth reviewer (%s dataset)" % repo_name)
    axes.set_xticks(ind + width)
    axes.set_xticklabels(tuple(scenarios))

    plt.show()


def plot_average_k_acccuracy(repo_name, limit=None, k_values=range(1, 10)):
    scenarios = ["scenario%d" % d for d in range(1, 5)]
    fig, axes = plt.subplots()

    for s in scenarios:
        print("Now processing: %s" % s)

        sliding_accuracy = evaluation.calculate_average_accuracy_for_sliding_window_k(repo_name, scenario=s, k_values=range(1, 10), limit=limit)
        sliding_accuracy = [sliding_accuracy[k] for k in k_values]

        axes.plot(k_values, sliding_accuracy)

    axes.set_xlabel("k")
    axes.set_ylabel("Average Accuracy")
    axes.set_title("Average accuracy of methods (%s dataset)" % repo_name)
    axes.set_ylim((0.0, 1.1))

    plt.legend(scenarios)
    plt.show()


if __name__ == "__main__":
    plot_average_position("../help/")
    plot_average_k_acccuracy("../help/")
