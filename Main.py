import Compl
import Cuadratica

def Main():
    print(" |=Setup=|=Mode=|\n", 
           "|===1===|===2==|\n ")
    
    selection = input(" 1 or 2?: \n")
    
    if selection == "2": print("\n |=Complex=|=Stat=|=EQN=|=Table=|\n",
                                  "|====1====|===2==|==3==|===4===|\n")
        
    selection2 = input(" ")
    
    if selection2 == "1": Compl.Calculator()
       
    elif selection2 == "2": print("esta funcion no esta programada aun")
        
    elif selection2 == "3":print("\n |-anX+bnY=cn-|-anX+bnY+cnZ=dn-|-ax2+bx+c=0-|-ax3+bx2+cx+d=0-|\n", 
                                    "|------1-----|--------2-------|------3-----|--------4-------|\n")   
           
    selection_2_1 = input(" ")
    if selection_2_1 == "1": print("esta funcion no esta programada aun")
    elif selection_2_1 == "2": print("esta funcion no esta programada aun")
    elif selection_2_1 == "3": Cuadratica.F_Cuadratica()
    elif selection_2_1 == "4": print("esta funcion no esta programada aun")

Main()
