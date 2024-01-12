# pipx, poetry and the issues of package management in python

Important note:
* the steps presented here are personal "best-practices" preferences.
* there are constant and frequent updates in the python ecosystem and these practices are subject to changes.
* always read the official documentation of the tools you use and install from trusted sources.
These are basic steps for a development environment. Advanced users may skip to last section.     

## What is pipx
Read from the [official site.](https://pipx.pypa.io/stable/)  
`pipx` is a tool for installing and running Python applications in isolated environments.    
It's a way to manage Python-based command line tools.   
Install pipx:   
```
python -m pip install --user pipx
python -m pipx ensurepath
``` 
The first command installs pipx.   
The second command ensures that the PATH is correctly configured to include the pipx installed packages.

## What is poetry
Read from the [official site.](https://python-poetry.org/)

## Install poetry
```
pipx install poetry
```

Check if install worked ok:
```bash
poetry --version
```

  
Read the [installation docs](https://python-poetry.org/docs/#installing-manually) for more.  

Create a virtual environment and activate it.  

Then install `setuptools` and `wheel`.  
 ```bash
 (.venv) \path\user\dev_boilerplate_course> pip install --upgrade setuptools wheel
 ````


## Use poetry to add python packages in the virtual environment.
**Remember to activate the virtual environment.**

Then initialize poetry inside the folder: `dev_boilerplate_course`.  
Read the prompt carefully.  
You may initialize a project interactively or non-interactively.  
To use poetry in a project, you need to initialize it first.    
Initialize poetry in the project folder, in the same directory that contains the .git folder.  
**Suggestion:**     
Place in the same directory level the following folders and files:
```
.git
.gitigonre    
.venv  
.idea
pyproject.toml
poetry.lock
```

To initialize poetry interactively, use the command:  
```bash
poetry init
```  
To initialize poetry non-interactively, use the command:  
```bash 
poetry init --no-interaction
```
or simply:
```bash
poetry init -n
```  
These commands will initiate `poetry` and create a `pyproject.toml` file.  
Suggestion: Don't set dependencies interactively.


## First commands to know
Read the [docs](https://python-poetry.org/docs/)

```bash
poetry init
poetry add <package_name> <package_name> <package_name>
poetry remove <package_name> <package_name> <package_name>
poetry install
```

## Edit pyproject.toml file
Use Pycharm or any other editor.   
**Leave author name to empty to avoid conflicts in repo**  

## Advanced topics
The steps above are just basic steps for a development environment.   
If you feel comfortable with the steps presented here, you are encouraged to explore more advanced tools and practices such as:  
* Using `.direnv` to automate the activation of the virtual environment when opening a directory.
* Create a bash scripts to automate the creation of:  
  * the virtual environment, 
  * the git repo,
  * the .direnv file and the environment variables.
    For examples see the [these bash related files.](https://github.com/argythana/newdot/tree/master/common)
  * for combining python and non-python tools in a project it is recommended to use a conda environment.    
    This is extremely helpful when working with LLMs.
    Please visit the [official conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more info.  

Advanced users are encouraged to visit this repo: [newdor](https://github.com/argythana/newdot) for more info.

You may use [starship](https://starship.rs/) to customize your prompt colours, style and information like this:
```bash
dev_boilerplate_course on  main [»!+] is 📦 v0.1.0 via 🐍 v3.10.12 
````
