"""
The code defines two functions for solving quadratic and cubic equations.
"""
import numpy as np
import math
from sympy import *

def selection():
    print("\n |-1.anX+bnY=cn-|-2.anX+bnY+cnZ=dn-|-3.ax2+bx+c=0-|-4.ax3+bx2+cx+d=0-|\n")
    user_input = input(" ")
    if user_input == "1": print("esta funcion no esta programada aun")
    elif user_input == "2": print("esta funcion no esta programada aun")
    elif user_input == "3": F_Cuadratica()
    elif user_input == "4": F_Cubica()
    else: ("invalid input") 
    
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
    print("\nAx3 + Bx2 + Cx + D = 0\n",
          "========================")
    A = float(input("insert first term: "))
    B = float(input("insert second term: "))
    C = float(input("insert third term: "))
    D = float(input("insert fourth term: "))
    
    
 
     
   