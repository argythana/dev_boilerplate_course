"""
Lecture Notes on defining functions
author: Argyriou Thanasis, email: argythana@gmail.com
date: Dec 2023

Decomposition, abstraction, reuse-ability, modularity, readability.
Similar to math => processes, output depends on parameters' value
Arguments (args) = formal parameters, args' values (= parameters' values).
> help(<FUNCTION NAME>) for args and values.
> syntax: def name(arg1, arg2, ..., argumentN): 
    docstrings (documentation, 2nd line, triple quotes)
    body = statements (what to do)
    return (what to return)
> Keyword args => "Default values" assign in definition.
> Positional args => require value assign in call.
> TypeError: missing required positional argument.
> Calling functions 
"""

### Change default paremeters' value of print()
##print('Comma print output', end=', ')


# define function
def message_simple(message="Python is great"):
    """
    A simple function with 1 argument and default value.
    :param message: string
    :return: None
    Trivial example, 1 argument, default value=Python is great\n"""
    print(message)


# documentation:
# print(message_simple.__doc__) # No parentheses

# Call with default or other value
print('Calling "message_for_you()" with default and other value:')
message_simple()
message_simple("Python is boring!")
# message_simp(message='Python is boring!') # same result


# 3 args, 2 non-default, 1 default value
# define positional args before keyword (else => SyntaxError)
# output and definition order flexibility
def message_from_to(sender, receiver, message="Please study\n"):
    """
    A function with 3 arguments, 2 non-default, 1 default.
    :param sender: string
    :param receiver: string
    :param message: string
    :return: None
    Print message from sender to receiver
    3 args, 1 default. Assign values to sender, receiver
    """
    print(sender, message, receiver)  # bad order, still works


# call message_from_to()
print("\nCalling 'message_from_to()' assigning values:")
message_from_to("Thanasis", "students", "kindly asks you to study Python, please, my excellent, ")

## which is "wrong", why ?
# message_from_to('Students:', 'Thanasis', 'No way',)
# message_from_to('Students:', 'No way', 'Thanasis')
print()


def bill(q, items, p):  # no object type specified
    """
    Print bill for quantity of items and price.
    Args:
        q: Quantity
        items: Item name
        p: Price
    Returns:
        None
    """
    total = q * p
    print(f"{q} {items}, cost {total} \n")  # match definition order


bill(3, "books", 10)

# keyword args match definition, flexible order
# bill(items='books', p=10, q=3)


# arbitrary number of args *
def multiply(*my_data):
    """ Multiply arbitrary number of args"""
    s = 1  # neutral factor
    for n in my_data:
        s *= n
    print(s)


multiply(1, 2, 3, 4, 5, 6)
