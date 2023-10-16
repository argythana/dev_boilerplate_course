# Learn poetry

## What is poetry
Read from the [official site.](https://python-poetry.org/)  


## Install poetry
Make sure venv is activated.  
First install `setuptools` and `wheel`.  
 ```bash
 (.venv) \path\user\dev_boilerplate_course> pip install --upgrade setuptools wheel
 ````


Install poetry with activated virtual environment, using pip.
```cmd
(.venv) \path\user\dev_boilerplate_course> pip install poetry 
```

check if install worked ok:

```bash
poetry --version
```

If you encounter issues, reinstall without activating virtual environment.   
This will install poetry for all users.   
Read the [installation docs](https://python-poetry.org/docs/#installing-manually) for more.  

## Use poetry to add python packages in the virtual enviroment.
**Activate the virtual environment.**

Then initialize poetry in `dev_boilerplate_course`.
Read the prompt carefully.  
Don't set dependencies interactively.   
**Leave author name to empty to avoid conflicts in repo**


```bash
poetry init
```


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

Your directory should look like this:  
```
dev_boilerplate_course
    ├── pyproject.toml
    ├── poetry.lock
    ├── .git
    │   └── ...
    ├── .venv
    │   └── ...
    ├── .gitignore
    ├── .idea
    ├── src
        └── data
```

## First commands to know
Read the [docs](https://python-poetry.org/docs/)

```bash
poetry init
poetry add <package_name>
poetry remove <package_name>
poetry install
```

## Edit pyproject.toml file
Use Pycharm or any other editor.   

**Leave author name to empty to avoid conflicts in repo**
