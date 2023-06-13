import numpy as np
import math

def F_Cuadratica():
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
            print(X1, X2) 
        except ValueError:
            break
    
# x1 = 1+3i, x2 = 1-3i
