import math

def secante(f, x0, x1, tol, itera):
    fx0 = f(x0)
    if(fx0 == 0):
        print( str(x0)+" es raiz")
    else:
        fx1 = f(x1)
        cont=0
        error=tol+1
        den = fx1 - fx0
        print("xn "+str(x1)+ " fnx "+ str(fx1))
        print("xn "+str(x0)+ " fnx "+ str(fx0))
        while((fx1!=0) and (error > tol) and (cont<itera) and (den!=0)):
            xc = x1 - (f(x1)*(x1-x0))/(den) 
            error = abs((xc - x1)/xc)
            x0 = x1
            fx0 = fx1
            x1 = xc
            fx1 = f(x1)
            den = fx1 - fx0
            print("xn "+str(xc)+ " fnx "+ str(fx1)+ " error "+ str(error))
            cont = cont + 1

        if(fx1 == 0):
            print(str(x1)+" es la raiz")
        elif(error<tol):
            print(str(x1)+" es un valor aproximado a una raiz con un error de "+str(tol))
        else:
            print("fracaso en "+str(itera)+" iteraciones")

        
def main():
    x0 = input("x0\n")
    x1 = input("x1\n")
    tol = input("tolerancia\n")
    ite = input("iteraciones\n")
    f = lambda x: math.exp(x) - 5*x + 2  #function here
    secante(f, float(x0), float(x1), float(tol), int(ite))
    
    
main()


