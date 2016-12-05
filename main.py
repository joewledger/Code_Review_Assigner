import os
import subprocess
import argparse
from collections import OrderedDict

import Code_Review_Assigner.parse_git_log as pgl
import Code_Review_Assigner.code_review_ranking as crr
import Code_Review_Assigner.plotting as plt

parser = argparse.ArgumentParser(description="Launcher for Code Review Assigner and utilities. Requires \'git\' in system PATH.")
subparsers = parser.add_subparsers(dest="command")

checkout_parser = subparsers.add_parser("checkout")
checkout_parser.add_argument("-r","--repo", type=str, help="Specify relative path to existing local git repo", required=True)

ranking_parser = subparsers.add_parser("ranking")
ranking_parser.add_argument("-r","--repo", type=str, help="Specify relative path to existing local git repo", required=True)
ranking_parser.add_argument("-s","--samplesize", type=int, help="Specify the sample size of commits to generate reviewers", default=None)
#ranking_parser.add_argument("-o","--output", type=str, help="Specify output image file (Default: 'output.png')", default ='output.png')

accuracy_parser = subparsers.add_parser("accuracy")
accuracy_parser.add_argument("-r","--repo", type=str, help="Specify relative path to existing local git repo", required=True)
accuracy_parser.add_argument("-s","--samplesize", type=int, help="Specify the sample size of commits to generate reviewers", default=None)
accuracy_parser.add_argument("-k", help="Specify a range of sliding k values (Default: '1,10')", default='1,10')
#accuracy_parser.add_argument("-o","--output", type=str, help="Specify output image file (Default: 'output.png')", default='output.png')

reccomend_parser = subparsers.add_parser("reccomend")
reccomend_parser.add_argument("-r","--repo", type=str, help="Specify relative path to existing local git repo", required=True)
reccomend_parser.add_argument("-c","--commitguid", type=str, help="Specify commit guid to generate reviewers", required=True)

def main():
    args = parser.parse_args()
    
    if(args.command == "checkout"):
        checkout_all(args.repo)
        git_log_output()

    elif(args.command == "reccomend"):
        history = pgl.parse(os.getcwd() + "//" + args.repo + "//")
        reviewers = crr.code_review_ranking(args.commitguid, history)
        sortedReviewers = sorted(reviewers, key=reviewers.__getitem__, reverse=True)
        print("Reccomended Reviewers:")
        for r in sortedReviewers:
            print("{0:0.1f}".format(reviewers[r]),":",r)
        groundtruth = min(history.commitIDMap[args.commitguid].reviewers) # literally one element
        print("\nGround Truth: " + groundtruth)
        print("Position of ground truth reviewer: " + str(sortedReviewers.index(groundtruth)+1))

    elif(args.command == "ranking"):
        plt.plot_average_position("plots/%s_ranking.png" % args.repo, args.repo, limit=args.samplesize)

    elif(args.command == "accuracy"):
        minmax = args.k.split(',')
        min = int(minmax[0])
        max = int(minmax[1])
        plt.plot_average_k_acccuracy("plots/%s_accuracy.png" % args.repo, args.repo, k_values=range(min, max), limit=args.samplesize)

def checkout_all(submodule_dir):
    os.chdir(submodule_dir)

    currentbranch = str(subprocess.check_output(
        "git rev-parse --abbrev-ref HEAD", shell=True), 'utf-8')

    output = str(subprocess.check_output(
        "git branch --all", shell=True), 'utf-8')

    branches = {n[n.rfind("/") + 1:] for n in output.split("\n")
                if n.strip().startswith("remotes")}
    for branch in branches:
        try:
            output = subprocess.check_output("git checkout %s" % branch, shell=True)
        except:
            pass

    subprocess.check_output("git checkout %s" % currentbranch, shell=True)


def git_log_output():
    output = subprocess.check_output("git log", shell=True)
    print(output)


if __name__ == "__main__":
    main()
