"""
Lecture Notes on reusing functions
author: Argyriou Thanasis, email: argythana@gmail.com
date: Dec 2023
> return function objects.
> Scope, global and local variables, Namespaces
> importing a function
> if __name__ == '__main__':
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do?page=1&tab=votes#tab-top
"""


# If output to be used elsewhere: => use return statement
def draft_power(base, expo):
    result = base**expo
    data = (result, base, expo)
    # print(dir()) #local names
    # print(data) show local variable to main
    return data  # return values to global scope (any type)


draft_power(2, 3)  # call in interpreter
### return not printed, use other function for that
# print(data)
# print(type(draft_power(2,3)))


def use_power(to_double):
    result = to_double * 2
    print(result)


# doesnt work if return data is commented
use_power(to_double=draft_power(2, 5))


# uncomment to use functions, put files in same dir
import lecture_3b_hypot_module
import song_function

# hypot_module.hypot_calculator()
##song_function.generate_song()


# print(hypot_function.__name__)
print()

# print(dir()) #Without arguments, return list of names in the current local scope


def run_all():
    hypot_module.hypot_calculator_modular()  # local
    song_function.generate_song()  # local
    draft_power(2, 3)  # local


run_all()  # will not run if functions not imported
