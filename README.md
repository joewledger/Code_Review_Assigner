# Code Review Assigner
Using existing git repository with reviewer tags, Code Review Assigner will generate code reviewer recommendations.

## Getting Started
These instructions will get you a copy of the project up and running for development and testing purposes.

### Prerequisites
Install these dependencies before running the project.

    git
    python3
    numpy
    matplotlib


### Initialization
Add and initialize a submodule for the repository under testing. Alternatively, use one of the sample repositories.
    
    $ git submodule add URL
    $ git submodule init
    $ git submodule update


Fetch all branches for the repository under testing. This may take some time
    
    $ python3 main.py checkout -r REPO

At this point, you can generate a recommended reviewer set for a specific commit using the SHA hash of the commit.
    
    $ python3 main.py recommend -r REPO -c HASH

## Running the evaluation
The purpose of the evaluation is to generate reviewer recommendations for the set of all reviews. Two evaluation techniques are available.

### Average ground truth position
In this evaluation method, a bar graph is generated comparing the average position of the ground truth reviewer compared to the ordered list of recommended reviewers. Lower scores are better.
    
    $ python3 ranking -r REPO
Results are saved in ```plots/REPO_ranking.png```

### Average accuracy for sliding window k
In this evaluation method, a line graph is generated comparing the presence of the ground truth reviewer in the sliding-size ordered set of reviewers. Lower scores are better.
    
    $ python3 accuracy -r REPO [-k RANGE]
Results are saved in ```plots/REPO_accuracy.png```
