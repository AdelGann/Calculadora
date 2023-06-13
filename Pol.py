"""
This function takes a polynomial expression as input, expands it, and prints the result.
"""
from sympy import *
def solve_poly():
    # if in input string you typed a wrong form of a polynomial probably will crash
    print("example: (2*x+16)**2 + (4*x-15)**2")
    expression = input("Enter a polynomial expression: ")
    expression = sympify(expression)
    result = expand(expression)
    print(result)
