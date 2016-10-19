import os
import subprocess
#os.system("git log")


def checkout_all():
    output = str(subprocess.check_output(
        "git branch --all", shell=True), 'utf-8')

    branches = {n[n.rfind("/") + 1:] for n in output.split("\n")
                if n.strip().startswith("remotes")}
    for branch in branches:
        output = subprocess.check_output("git checkout %s" % branch, shell=True)


def git_log_output():
    output = subprocess.check_output("git log", shell=True)
    print(output)


# checkout_all("qtquickcontrols2")


if __name__ == "__main__":
    submodule_name = "qtquickcontrols2"

    os.chdir(submodule_name)
    checkout_all()
    git_log_output()
