"""
The function provides a menu-driven program that allows the user to select different modes and
functions related to complex numbers, statistics, equations, and more.
"""

import Compl
import Eqn
import Pol

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
    print(" |=1.Suceciones=|=2.polinomios=|=3.Derivadas=|=4.Integrales=|=5.Conjuntos=|\n",
           "|=6.Interes Compuesto=|=7.Ecuaciones Diferenciales=|=8.Sistemas no lineales=|=9.Sistemas de inecuaciones=|=10.Sistemas de ecuaciones lineales=|")
    print("only available 2")
    user_input = input(" ")
    if user_input == "1": print("not available")
    elif user_input == "2": Pol.solve_poly()
    

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


    


