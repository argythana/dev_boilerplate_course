## Before the lecture:

Download and install git from [the official page](https://git-scm.com/)

Download and install github desktop


The source code for Git refers to the program as "the information manager from hell" (from wikipedia)


## In the lecture, goals for learning.

My main points for using git:
a) version control,
b) collaboration,
c) storage,
c) small steps to success. 

The advantages of git: https://git-scm.com/about


Main lecture goal: 
Create a new repo, make some commits to it, publish it on github.

## Use commands:
git init
git status
git diff
git add
git commit -m "Consice and explanatory message."

git push (publish to github)

modify file

git status
git diff
git add
git commmit
git push (to github, use github desktop)

git branch
git branch --list

git branch new_branch_name
git checkout branch_name

show gitk
show git-gui

## Understand the meaning of what happens when working on a branch.
"The working tree and the index are updated to match the branch. All new commits will be added to the tip of this branch."

## Demonstrate using windows explorer and switching branch, gitgwhy git works as a "multidimensional parallel universe" (tm) for your files. 

## After the lecture:

### For studying:
1) Read and try the commands you learned form the official git documentation: https://git-scm.com/doc
For example search in the official site: "git commit" https://git-scm.com/docs/git-commit
Even better: use the --help command.
For example: git init-help

2) Read and try the commands you learned form the official github documentation: https://docs.github.com/en




3) Must read: https://en.wikipedia.org/wiki/Git
For your training:
Create some test repos, make changes, add changes, commit, push,.
[repo_init](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)


[repo_naming](https://github.com/bcgov/BC-Policy-Framework-For-GitHub/blob/master/BC-Gov-Org-HowTo/Naming-Repos.md)



### Tasks to absolutely do for succesful completion of the course:
1) After I invite you: Fork my repo locally on your PC. Do this inside a folder called "dev_boilerplate_course"

2) create a new_branch with your your_firstname_lastname_abbrev (use a 4 to 8 letters abbreviation, e.g. thanarg).
You may use any nick you want to be know us a hacker. e.g. "blue_cat"

Do this inside a folder called: 
"dev_bp_fork_your_firstname_lastname_abbrev"
This will be your branch to work on for the course.


3) Put inside your branch of the repository a new file with questions or comments.

4) Do a pull request so that I include your branch as part of the repo.
Read this: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork


For further reading:
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests


5) create a .gitignore file [next to .git](https://stackoverflow.com/a/19098654)

```  

type nul > .gitignore   

```
