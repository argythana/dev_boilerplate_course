## Directory Structure and file hierarchy  

**Suggestion:**   
Place in  the same directory level the following folders and files:  

```
.git
.gitigonre    
.venv  
.idea
pyproject.toml
poetry.lock
```

On linux OS try the commands:   
`tree` in the terminal to see the directory structure.
`tree -a` in the terminal to see all files and folder within the directory structure.
`tree -a -F` in the terminal to see all files and folders within the directory structure.

On Windows OS try the commands:  
`tree` in the terminal to see the folders the directory structure.
`tree /F` in the terminal to see all files and folder within the directory structure.  
`tree /A /F` in the terminal to see all files and folders within the directory structure.

Generally, the directory structure should look like this:  

```bash 
 - dev_boilerplate_course (folder)
    ├── pyproject.toml (poetry config file)
    ├── poetry.lock (poetry lock file)
    ├── .gitignore (file)
    ├── README.md (file)
    ├── .git (folder)
        └── ... (git files folders)
    ├── .venv (folder)
    │   └── ... (virtual environment files)

    ├── .idea (PyCharm config files folder)
    ├── src (source code folder)
        ├── *.py (python scripts files)
        └── data (folder with data files)
        └── students_work (folder with students files)
            └── student A (student A files)
            ├── student B (student B files)
            ├── ... ... 
            └── student Z (student Z files)
```
