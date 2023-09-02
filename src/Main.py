"""
The function provides a menu-driven program that allows the user to select different modes and
functions related to complex numbers, statistics, equations, and more.
"""

import Compl
import Eqn
import Pol
import Stat

def setup(): # setup probably was a function that will return a setting table for the calculator
    pass

def mode():
    print("\n|=1.Complex=|=2.Stat=|=3.EQN=|=4.Table=|\n")
    user_input = input("[|]: ")
    match user_input:
        case "1": Compl.Calculator()
        case "2": Stat.Main()
        case "3": Eqn.Main()
        case "4": print("Not programmed yet.")
        case _: print("Try again.")

def more_functions():
    print("""   |=1.Suceciones=|=2.polinomios=|=3.Derivadas=|=4.Integrales=|=5.Conjuntos=|
   |=6.Interes Compuesto=|=7.Ecuaciones Diferenciales=|=8.Sistemas no lineales=|=9.Sistemas de inecuaciones=|
   |=10.Sistemas de ecuaciones lineales=|""")

    print("only available 2")
    user_input = input("[|]: ")
    match user_input:
        case "1": print("opcion invalida")
        case "2": Pol.solve_poly()
        case _: print("opcion invalida")
    

def start():
    print("|=1.setup=|=2.mode=|=3.more functions=|\n")
    user_input = input("[|]: ")
    match user_input:
        case "1": setup()
        case "2": mode()
        case "3": more_functions()
        case _: print("invalid input")

def main():
    start()

main()
