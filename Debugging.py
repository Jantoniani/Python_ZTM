# Debugging

# Linting - allows us to detect, as we code, issues with our code
# Use an Editor or IDE (such as PyCharm)
# Learn to read errors and understand what they mean
# pdb or Python Debugger - gives you an interactive debugger


# pdb example

import pdb


def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2


add(4, 'evervre')
