"""
Lecture Notes on defining functions
author: Argyriou Thanasis, email: argythana@gmail.com
date: Dec 2023
from math import sqrt  # import only sqrt => no reference math module when called
"""

def myhypot(x, y):
    """CALCULATE hypotenuse. Assign values for x, y."""
    hyp = sqrt(x * x + y * y)  # no reference to math
    return hyp  # hyp = local var


def hypot_calculator_modular():
    """Ask for triangle sides and PRINT hypotenuse. Works if input is numbers"""
    a = float(input("Insert side a: "))
    b = float(input("Insert side b: "))
    H = myhypot(a, b)  # call function hyp()
    print("Hypotenuse = ", H)


if __name__ == "__main__":  # syntax for stand alone executable script.
    hypot_calculator_modular()  # will be called when run as an executable script.
    print(
        "Wow, a stand-alone script? Wow! You are only 984 steps away from becoming a developer.\
    \nYou can do it! Just take 5 small steps each day!"
    )


# print(__name__)

# if line below is uncommented:
# hypot_calculator_modular()

# hypot_calculator_modular() will be called when the module is imported.
# hypot_calculator_modular() will be called twice when this file is Run as a stand alone script.
