## Before the lecture:

Download and install git from [the official page](https://git-scm.com/)

Download and install GitHub desktop


The source code for Git refers to the program as "the information manager from hell" (from wikipedia)


## In the lecture, goals for learning.

My main points for using git:
- a) version control,
- b) collaboration,
- c) storage,
- d) small steps to success. 

The advantages of git: https://git-scm.com/about


Main lecture goal: 
Create a new repo, make some commits to it, publish it on GitHub.

## Use commands:
```bash
git init  
git status  
git diff  
git add  
git commit -m "Concise and explanatory message."  
git log
```

git push (publish to GitHub)  

Then modify a file and go through these commands again.  

```bash
git status  
git diff  
git add  
git commit  
git push (to GitHub, use GitHub desktop)  

git branch
git branch --list

git branch new_branch_name  
git checkout branch_name  
```


Also show the usage of gitk, git-gui, GitHub desktop.

## Understand the meaning of what happens when working on a branch.
"The working tree and the index are updated to match the branch. All new commits will be added to the tip of this branch."

## Demonstrate using "windows file explorer" and switching branch, gitg, gitk, why git works as a "multidimensional parallel universe" (TM) for your files.   

## After the lecture:

### For studying:
1) Read and try the commands you learned form the [official git documentation:](https://git-scm.com/doc)  
For example search in the official site: ["git commit"](https://git-scm.com/docs/git-commit)    
Even better: use the --help command.  
For example: git init-help  

2) Read and try the commands you learned form the official [GitHub documentation](https://docs.GitHub.com/en)  


3) Must read: https://en.wikipedia.org/wiki/Git
For your training:  
Create some test repos, make changes, add changes, commit, push.  
[How to initialize a git repository](https://docs.GitHub.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-GitHub)  


[Suggested best practices for repository naming](https://GitHub.com/bcgov/BC-Policy-Framework-For-GitHub/blob/master/BC-Gov-Org-HowTo/Naming-Repos.md)



### Tasks to absolutely do for successful completion of the course:  
Note! For each change that you think is ok, do all the process step by step:   
**add, commit with message, push**   

1) After I invite you: Fork my repo locally on your PC. Do this inside a folder called `"dev_boilerplate_course"`  
Read [about repository forks.](https://docs.GitHub.com/en/get-started/quickstart/fork-a-repo)  

2) On your local PC, in the repository fork, create a new branch with your `your_firstname_lastname_abbrev` (use a 4 to 8 letters abbreviation, e.g. `thanarg`).  
You may use any nick you want to be known as a hacker. e.g. `"blue_cat"`   

Do this inside the forked repository.   
This will be your branch to work on for the course.   

3) Put inside your branch of the repository a new file with questions or comments.   

4) Do the exercise that is described in the `playground_file.txt`.  

5) Do a pull request so that I include your branch as part of the repo.
Read [this on pull requests.](https://docs.GitHub.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)  


[Further reading on collaborating with pull requests.](https://docs.GitHub.com/en/pull-requests/collaborating-with-pull-requests)  


5) create a .gitignore file [next to the `.git` folder](https://stackoverflow.com/a/19098654)  
With the command below you create an empty file called `.gitignore` just by using only the cli.   

```bash
type nul > .gitignore   
```
