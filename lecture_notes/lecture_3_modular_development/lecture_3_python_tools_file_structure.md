## Lecture 3 Python: functions, modular development, project structure, dev tools.

Get first basic understanding of the following:

1. Define functions:  
* Do one thing only. Using "and" is smelly.
* Naming
* Arguments
* Type Hints
* Doc strings
* Return
* Call other functions in a function.  

2. User made python "modules".

* different file to define useful functions.
* different file to run a project script.
* Usage of: `if __name__ == "__main__":`

3. Use relative paths.
* for data files.
* for main script to run.

4. Python dev tools.
* black (style formatter)
* ruff (code linter)
* Automate usage in Pycharm.
* or run from the command line.


5. Basic usage of `streamlit`.
* sliders
* charts.
* update code.
* update users view.


## How to practice:  

1) Use a new jupyter notebook to:    
a) sum activities distance by date.  
b) Create a plotly chart for this.  
c) Create a streamlit app for this chart.  
Do this cell after cell in many single line commands.    

2) Define new different functions to do all this a new `.py` file.  
And in the end a function that calls all these function and creates the streamlit app.  

3) Create a different file to run and create the streamlit app in few lines of code.