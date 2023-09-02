"""
The code defines two functions for solving quadratic and cubic equations.
"""
import numpy as np
import math
from sympy import * 
import os

def Main():
    print("\n |-1.anX+bnY=cn-|-2.anX+bnY+cnZ=dn-|-3.ax2+bx+c=0-|-4.ax3+bx2+cx+d=0-|-5.Lineal Eq-|\n")
    user_input = input(" ") 
    match user_input:
        case "1": "esta funcion no esta programada aun"
        case "2": "esta funcion no esta programada aun"
        case "3": F_Cuadratica()
        case "4": F_Cubica()
        case "5": F_Lineal_Eq()
        case _: "invalid input"
    
def F_Cuadratica():
    print("\n Ax2 + Bx + C = 0 \n", 
             "================")
    
    while True:
        try: 
            print("Insertar los terminos")
            A = float(input("A = "))
            B = float(input("B = "))
            C = float(input("C = ")) 
            discriminante = B * B - 4 * A * C
            if discriminante < 0:
                sqrtC = math.sqrt(-discriminante)
                X1 = complex(-B / (2 * A), sqrtC / (2 * A))
                X2 = complex(-B / (2 * A), -sqrtC / (2 * A))
            else:
                sqrt = math.sqrt(discriminante)
                X1 = round((-B + sqrt) / (2 * A), 2)
                X2 = round((-B - sqrt) / (2 * A), 2)
            print(X1, X2,"\n") 
        except ValueError:
            break
    
def F_Cubica():
    x = symbols('x')
    while True:
        try:
            a = float(input("Enter the first term: "))
            b = float(input("Enter the second term: "))
            c = float(input("Enter the third term: "))
            d = float(input("Enter the fourth term: "))

            cubic_equation = a*x**3 + b*x**2 + c*x + d
            solved = solve(cubic_equation, x)

            print(cubic_equation, solved)
        except ValueError: break
            
    
    
def F_Lineal_Eq():
    while True:
        try:
            expression = (input("insert lineal equation: "))
            print(solve(expression))
        except ValueError:
           break
     
os.system("pause")
