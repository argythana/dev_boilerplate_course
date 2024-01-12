# Welcome to the "Research Methods - Software Development Tools" Crash-Course!

This repository provides a concise presentation of some necessary tools for a data-centric python development environment.  
It has been created for the University of Athens, Department of Economics, [MSc. in Business Administration, Analytics and Information Systems](https://bis-analytics.econ.uoa.gr/) Postgraduate Program.  
The course has been created, is being curated and taught by [Thanasis Argyriou, @linkedin](https://www.linkedin.com/in/thanasis-argyriou-06155a94/).  

It is a **crash-course** on some necessary development tools, as part of the "Research Methods" seminars of the third semester.    
This is **not** a complete guide, but rather a quick start tutorial on principles and foundational concepts with practical examples.  
All tools are used as examples, not as necessary endorsements.    
The material is in the form of a GitHub repository and is also available on e-class: [Research Seminars sub-course](https://eclass.uoa.gr/courses/ECON875/).  

Excellent working knowledge of the previous second semester courses is assumed:   
* "[Python for Analytics, Data Science and Machine Learning](https://eclass.uoa.gr/courses/ECON537/)",
* "[Machine Learning](https://eclass.uoa.gr/courses/ECON608/)"
* SQL.

Necessary prerequisites are:
* creating python virtual environments and installing python packages, 
* working with Python editors and Jupyter Notebooks, 
* Markdown language and,
* Windows (or Linux) Command Line Interface.  
* Understanding of basic concepts of relational and non-relational databases.
* Understanding of basic concepts of working from "relative" or "absolute" OS paths.

Students are kindly encouraged to register and read the material before the first lecture.  
**Important things to do before the first lecture:**   
There are great free resources for students at [GitHub Education](https://education.GitHub.com/).  
* Explore the offers at the [GitHub student developer pack](https://education.GitHub.com/pack).    
* Sign up for a GitHub account.  
* Install [PyCharm IDE](https://www.jetbrains.com/pycharm/).  
* Activate [GitHub copilot](https://github.com/features/copilot/).  
* Register for `Digital Ocean` credits.
* Get a `Name Cheap` domain name.   


The material is presented in four live (3 hours long) seminars and two (optional and advanced) async lectures.     
Each lecture requires 9 hours for self-study and 8 hours for practice on tasks/assignments.   
The pace is intensive by design and each lecture requires good working knowledge of all the previous ones.    
Therefore, it is highly recommended to complete the tasks and assignments before each following lecture and attend all lectures.  

Support is provided on a personal basis via the e-class platform, the GitHub repository and "on-demand" meetings.    
Announcements are made via the e-class platform.    
The course is graded with a final in-person exam.

## Goals:  
At the end of the course, students should be able to:
* Work on a python virtual environment.
* Use a version control system like git, manage local and remote repositories and work collectively on a repo.
* Use a python package manager like poetry to pin python version and package dependencies.
* Use a python linter like ruff to check code quality.
* Use a python code formatter like black to format code style.
* Use a python IDE like PyCharm to develop python code.
* Use GitHub copilot to help with code suggestions, completions, documentation.
* Use SQL and SQLAlchemy to interact with relational databases.
* Use MongoDB and pymongo to work on non-relational databases.
* Combine the tools above to work on a more productive/efficient a python development environment.

The tools presented are:  

## Lecture 1: Version control tools
Secure Code Development, version control, repository management.
1) [Git](https://git-scm.com/)  
2) [GitHub](https://github.com/)
3) gitk, git bash, git cli, git GUI, GitHub Desktop.  
4) .gitignore file.

## Lecture 2: Python development tools, virtual environment and package management
Modular, reusable code development. Creating modules, file hierarchy, project structure.    
Advanced editing combining PyCharm, GitHub copilot, Black, Ruff.  
1) [Integrated Development Editors: PyCharm IDE](https://www.jetbrains.com/pycharm/)
2) Integrate GitHub copilot in PyCharm IDE (https://copilot.GitHub.com/)
3) [Python Package Management: using Poetry](https://python-poetry.org/)
4) [Python linter and code formatter: Ruff](https://github.com/astral-sh/ruff)
5) [Python code formatter: Black](https://github.com/psf/black)

## Lecture 3: Modular development: build a Streamlit App
Interactive web apps with Python. Training on real data and tasks examples.  
Use a *.csv data file and pandas to create a streamlit app.   
1) [Streamlit](https://streamlit.io/)
2) [Streamlit Gallery](https://streamlit.io/gallery)
3) [Streamlit Documentation](https://docs.streamlit.io/en/stable/)
4) [Streamlit Cheatsheet](https://docs.streamlit.io/library/cheatsheet)

## Lecture 4: MongoDB tools
Non-Relational and schema-less Databases (MongoDB) with Python. Training on real data and tasks examples.  
Use a mongoDB database with the same data and pymongo to create a streamlit app. 
1) [MongoDB](https://www.mongodb.com/)
2) [MongoDB Compass](https://www.mongodb.com/products/compass)
3) [MongoDB Shell](https://www.mongodb.com/products/shell)
4) [MongoDB Database Tools](https://www.mongodb.com/products/database-tools)
5) [MongoDB Python Driver](https://docs.mongodb.com/drivers/python/)
6) [MongoDB Python Driver PyMongo](https://pypi.org/project/pymongo/) 


## Asynchronous education (optional, self-paced): SQL tools
Working on Relational (SQL) Databases with Python. Training on real data and tasks examples.  
Use an SQL database with the same data to create a streamlit app.
1) [SQLAlchemy](https://www.sqlalchemy.org/)
2) [SQLite](https://www.sqlite.org/index.html)
3) [SQLite Python Driver](https://docs.python.org/3/library/sqlite3.html)
4) [PostgreSQL](https://www.postgresql.org/)
5) [MySQL](https://www.mysql.com/)
6) [MySQL Python Driver](https://dev.mysql.com/doc/connector-python/en/)


## Asynchronous education (optional, self-paced): Remote linux servers
Interact from local PC on a Linux Remote Server using the Command line.   
Secure access, SSH, install necessary software, create automated system services and timers, manage logs.  
Deploy a mongoDB database on a remote linux server.  
Deploy a streamlit app on a remote linux server.  
1) Secure Shell protocol  
* [Secure Shell - SSH](https://www.ssh.com/academy/ssh)
* [SSH Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)  
* [SSH on linux](https://wiki.archlinux.org/title/OpenSSH)   
* [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)  
2) Secure Copy Protocol
* [SCP](https://www.ssh.com/academy/ssh/scp)  
* [SCP on linux](https://wiki.archlinux.org/title/SCP_and_SFTP)  
3) Rsync utility
* [RSYNC on wikipedia](https://en.wikipedia.org/wiki/Rsync)
* [RSYNC on linux](https://wiki.archlinux.org/title/Rsync)
4) Systemd 
* [Linux Systemd](https://wiki.archlinux.org/title/Systemd)

Thank you very much for your interest and have fun on your journey on programming and data science!  
