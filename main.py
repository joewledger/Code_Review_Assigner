import os
import subprocess
import argparse
from collections import OrderedDict

import Code_Review_Assigner.parse_git_log as pgl
import Code_Review_Assigner.code_review_ranking as crr

parser = argparse.ArgumentParser(description="Launcher for Code Review Assigner and utilities. Requires \'git\' in system PATH.")

parser.add_argument("-ch","--checkoutall", help="Download all branches for specified repo (may take some time)", action="store_true")
parser.add_argument("-r","--repo", type=str, help="Specify relative path to existing local git repo")
parser.add_argument("-c","--commitguid", type=str, help="Specify guid for commit to generate reviewers")
parser.add_argument("-a","--all", help="Generate reviewers for all valid commits", action="store_true")
parser.add_argument("-o","--output", type=str, help="Specify output file")
parser.add_argument("-k", type=int, help="Specify the max number of reviewers to generate (Default: 10)", default=10)


def main():
    args = parser.parse_args()
    
    if args.checkoutall:
        if args.repo:
            checkout_all(args.repo)
            git_log_output()
        else:
            print("Error: Specify a repo with -r")

    else:
        if args.repo:
            if args.commitguid:
                history = pgl.parse(os.getcwd() + "//" + args.repo + "//")
                reviewers = crr.code_review_ranking(args.commitguid, history, method="LCSubseq", scenario="scenario4")
                sortedReviewers = sorted(reviewers, key=reviewers.__getitem__, reverse=True)[:args.k]
                for r in sortedReviewers:
                    print("{0:0.1f}".format(reviewers[r]),":",r)
            elif args.all:
                #TODO: return (and probably output) the results for every commit 
                history = pgl.parse(os.getcwd() + "//" + args.repo + "//")
            else:
                print("Error: Specify a commit with -c, or use -a to specify all commits")
        else:
            print("Error: Specify a repo with -r")

def checkout_all(submodule_dir):
    os.chdir(submodule_dir)
    output = str(subprocess.check_output(
        "git branch --all", shell=True), 'utf-8')

    branches = {n[n.rfind("/") + 1:] for n in output.split("\n")
                if n.strip().startswith("remotes")}
    for branch in branches:
        output = subprocess.check_output("git checkout %s" % branch, shell=True)


def git_log_output():
    output = subprocess.check_output("git log", shell=True)
    print(output)


if __name__ == "__main__":
    main()
