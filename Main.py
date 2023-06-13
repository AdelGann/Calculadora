"""
The function provides a menu-driven program that allows the user to select different modes and
functions related to complex numbers, statistics, equations, and more.
"""

import Compl
    
import Eqn

def setup():
    pass

def mode():
    print("\n |=1.Complex=|=2.Stat=|=3.EQN=|=4.Table=|\n")
    user_input = input(" ")
    if user_input == "1": Compl.Calculator()
    elif user_input == "2": print("esta funcion no esta programada aun")
    elif user_input == "3": Eqn.selection()
    elif user_input == "4": print("esta funcion no esta programada aun")
    
def more_functions():
    print(" |=1.Derivadas=|=2.Integrales=|=3.Suceciones=|=4.Polinomios=|=5.Sistemas de ecuaciones lineales=|\n",
           "|=6.Conjuntos=|=7.Interes Compuesto=|=8.Ecuaciones Diferenciales=|=9.Sistemas no lineales=|=10.Matrices")
    
    print("Soon")

def start():
    print("|=1.setup=|=2.mode=|=3.more functions=|\n")
    user_input = input(" ")
    if user_input == "1": setup()
    elif user_input == "2": mode()
    elif user_input == "3": more_functions()
    else: print("invalid input")

def main():
    start()
main()


    


