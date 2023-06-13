"""
This is a calculator function that takes user input for an expression and evaluates it using the
numexpr library.
"""
import math   
from math import pi, e
import numexpr



def Calculator():
    while True:
        try:
            expression = input("Enter an expression to calculate: ")
            result = numexpr.evaluate(expression)
        except ValueError:
            print(result.item(0))
        except ValueError:
            print("Invalid expression. Please try again.")
            continue
            break

