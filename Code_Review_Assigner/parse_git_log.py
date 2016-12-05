# Purpose: This script accepts a (relative) folder path to a locally cloned git repository.
#          The script will retreive a log of all commits, and parse each commit into model.Commit objects.
# 
# Limitations: Commit subject messages may not contain ASCII chars 0x1d, 0x1e, 0x1f
#
# TODO: Reviewers must be parsed from the commit message

import subprocess
import os
import sys
from datetime import datetime
import commitHistory as ch

def parse(folderPath):
    # https://git-scm.com/docs/git-log search "format:<string>"
    # 'id', 'timestamp', 'author', 'subject', 'parents'
    GIT_LOG_FORMAT = ['%H', '%ad', '%an', '%b', '%P']
    GIT_LOG_FORMAT = '\x1d' + '\x1e'.join(GIT_LOG_FORMAT) + '\x1f'
    
    # http://blog.lost-theory.org/post/how-to-parse-git-log-output/
    # each commit output: "\x1d[commithash]\x1e[timestamp]\x1e[author]\x1e[subject]\x1e[parents]\x1f\n[filepath1]\n[filepath2]\n"
    pr = subprocess.Popen( 'git log --name-only --all --reverse --format="%s"' % GIT_LOG_FORMAT , cwd = os.path.dirname( folderPath ), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    (out,err) = pr.communicate()
    
    commits = out.decode('utf-8').split('\x1d')

    metadata = [commit.split('\x1f')[0].split('\x1e') for commit in commits]

    files = [commit.split('\x1f')[1].split('\n') if len(commit.split('\x1f')) > 1 else '' for commit in commits]
    
    history = ch.commitHistory(folderPath)
    
    for idx, metadatum in enumerate(metadata):
        if(metadatum[0] == ''):
            continue
        
        nextcommit = ch.Commit(metadatum[0])
        # https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
        nextcommit.timestamp = datetime.strptime(metadatum[1],'%a %b %d %H:%M:%S %Y %z')
        author = metadatum[2]
        author = "".join([x if ord(x) < 128 else '?' for x in author])
        nextcommit.authors.add(author)

        for line in metadatum[3].split('\n'):
            if "Reviewed-by: " in line:
                name = line[len("Reviewed-by: "):].split(" <")[0]
                name = "".join([x if ord(x) < 128 else '?' for x in name])
                nextcommit.reviewers.add(name)

        nextcommit.filePathsChanged = list(filter(None, files[idx]))
        nextcommit.parents = list(filter(None, metadatum[4].split(' ')))
        history.commitIDMap[nextcommit.id] = nextcommit
    
    return history

def revlist(folderPath, commitid):
    pr = subprocess.Popen( 'git rev-list %s' % commitid , cwd = os.path.dirname( folderPath ), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    (out,err) = pr.communicate()
    
    commits = list(filter(None,out.decode('utf-8').split('\n')))[1:]
    return commits

if __name__ == '__main__': parse('../help/')
