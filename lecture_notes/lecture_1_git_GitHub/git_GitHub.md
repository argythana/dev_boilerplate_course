## Before the lecture:

Download and install git from [the official page](https://git-scm.com/)  
Download and install `GitHub desktop`.

The source code for Git refers to the program as *"the information manager from hell"* (wikipedia).

## In the lecture, goals to explain.
Main points for using git:
- a) version control,
- b) collaboration,
- c) storage,
- d) small steps to success. 

The advantages of git: https://git-scm.com/about

Main lecture goals: 
Create a new repo, make some commits to it, publish it on GitHub.

## Use commands:
```bash
git init  
git status  
git diff  
git add  
git commit -m "Concise and explanatory message."  
git log
git remote    
done
```

Show which remote repo is connected to your local repo.  

```bash
git remote -v
```

**Show how to connect to remote repo (publish to GitHub) .**  

```bash 
git push 
```

Then modify a file and go through these commands again.  

```bash
git status  
git diff  
git add  
git commit  
git push  #(to GitHub, You may use GitHub desktop)  

git branch
git branch --list

git branch new_branch_name  
git checkout branch_name  
```

Try the usage of gitk, git bash, git cli, git GUI, GitHub Desktop with examples.   

## Understand the meaning of what happens when working on a branch.
"The working tree and the index are updated to match the branch".   
"All new commits will be added to the tip of this branch."

## Use "Windows file explorer" and switching branch, gitg, gitk, why git works as a "multidimensional parallel universe" (TM) for your files.   

## Demonstrate the usage of the .gitignore file

The first .gitignore file should be [next to the `.git` folder](https://stackoverflow.com/a/19098654).
With the command below you create an empty file called `.gitignore` just by using only the CLI.   

```bash
type nul > .gitignore   
```

Add the following lines to the `.gitignore` file:
```
# Ignore all files that end with .ipynb_checkpoints
.ipynb_checkpoints
# Ignore the virtual environment .venv folder
.venv
# Ignore the .idea (PyCharm setting) folder
.idea
# Ignore python cache files and .pyc files
__pycache__
*.pyc
```

## After the lecture:

### To study:
1) Read and try the commands you learned form the [official git documentation:](https://git-scm.com/doc)  
For example search in the official site: ["git commit"](https://git-scm.com/docs/git-commit)    
Even better: use the `--help` "switch".  
For example: `git init --help`   

2) Read and try the commands you learned form the official [GitHub documentation](https://docs.GitHub.com/en)  

3) Must read: https://en.wikipedia.org/wiki/Git


### To practice: 
Create some test repos, make changes, add changes, commit, push.  
[How to initialize a git repository](https://docs.GitHub.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-GitHub)  

[Suggested best practices for repository naming](https://GitHub.com/bcgov/BC-Policy-Framework-For-GitHub/blob/master/BC-Gov-Org-HowTo/Naming-Repos.md)

Try this [tool](https://git-school.github.io/visualizing-git/) to visualize git commands.

### Tasks to absolutely do for successful completion of the course:  
Note! For each change that you think is ok, do all the processes step by step:   
**add, commit with message, push**   

1) After I invite you:   
Clone my repo `locally` on your PC. Do this inside a folder called `"dev_boilerplate_course"`  

Read about repository cloning.
Read the difference between repository clones and [repository forks.](https://docs.GitHub.com/en/get-started/quickstart/fork-a-repo)  

2) On your local PC, in the repository fork, create a new branch with your `your_firstname_lastname_abbrev` (use a 4 to 8 letters abbreviation, e.g. `thanarg`).  
You may use any nick you want to be known as a hacker. e.g. `"blue_cat"`   

Do this inside the cloned repository.   
This will be your branch to work on for the course.   

3) Put inside your branch of the repository a new file with any questions or comments.   

4) Do the exercise that is described in the `playground_file.txt`.  

5) Do a pull request so that I include your branch as part of the repo.
Read [this on pull requests.](https://docs.GitHub.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
[Further reading on collaborating with pull requests.](https://docs.GitHub.com/en/pull-requests/collaborating-with-pull-requests)


7) Create a distinct folder with your GitHub username inside the `src/students_work` folder.  