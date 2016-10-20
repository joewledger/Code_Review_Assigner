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
from model.commitHistory import *

def parse(folderPath):
    # go here https://git-scm.com/docs/git-log search for this: "format:<string>"
    # GIT_LOG_FORMAT breaks down to 'id', 'timestamp', 'author', 'subject', 'parents'
    GIT_LOG_FORMAT = ['%H', '%ad', '%an', '%s', '%P']
    # the challenge is that "--format" does not allow specifications for file path diff information
    # therefore, we prepend, deliminate, and postpend the non-file diff data (metadata) with ASCII chars for parsing below
    GIT_LOG_FORMAT = '\x1d' + '\x1e'.join(GIT_LOG_FORMAT) + '\x1f'
    
    # See http://blog.lost-theory.org/post/how-to-parse-git-log-output/ for a good starting point
    # Note that "--name-only" adds support for displaying the file path names for each modified file
    pr = subprocess.Popen( 'git log --name-only --format="%s"' % GIT_LOG_FORMAT , cwd = os.path.dirname( folderPath ), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    (out,err) = pr.communicate()
    # below is a sketch of a single commit represented in the "out" string
    # note the seperating chars and locations of important data
    # "\x1d[commithash]\x1e[timestamp]\x1e[author]\x1e[subject]\x1e[parents]\x1f\n[filepath1]\n[filepath2]\n
    
    # split the output by the prepend \x1d char
    # http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
    commits = out.decode('utf-8').split('\x1d')
    # grab the metadata before the postpended \x1f char and then split it by the \x1e deliminator 
    metadata = [commit.split('\x1f')[0].split('\x1e') for commit in commits]
    # somestimes there may be diff files, sometimes not (ex. a merge may not have diff files)
    # therefore, if any data exists after the postpended \x1f char (len(split)>1), then split it by newline \n chars 
    # http://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
    files = [commit.split('\x1f')[1].split('\n') if len(commit.split('\x1f')) > 1 else '' for commit in commits]
    
    history = commitHistory()
    
    # this is not your grandpa's for loop http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
    for idx, metadatum in enumerate(metadata):
        # the split operation will have an ampty element for the first prepended \x1d char (pass over it)
        if(metadatum[0] == ''):
            pass
        else:
            nextcommit = Commit(metadatum[0])
            # https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
            nextcommit.timestamp = datetime.strptime(metadatum[1],'%a %b %d %H:%M:%S %Y %z')
            nextcommit.authors.add(metadatum[2])
            # TODO: parse "reviewed by" out of subject message, this is embedded in metadatum[3]
            # big debate on the next line http://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
            nextcommit.filePathsChanged = list(filter(None, files[idx]))
            nextcommit.parents = metadatum[4].split(' ')
            history.commitIDMap[nextcommit.id] = nextcommit
    
    return history

if __name__ == '__main__': parse('../help/')
