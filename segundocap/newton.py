import math

def newton(f, df, x0, tol, itera):
    fx=f(x0)
    dfx = df(x0)
    cont=0
    error=tol+1
    while((fx!=0) and (error > tol) and (cont<itera) and (dfx!=0)):
        xn = x0 - (fx/dfx)
        fx = f(xn)
        dfx = df(xn)
        error = abs((xn - x0)/xn)
        print("xn "+str(xn)+ " fnx "+ str(fx)+ " err "+str(error))
        cont = cont + 1
        x0 = xn

    if(fx == 0):
        print(str(x0)+" es la raiz")
    elif(error<tol):
        print(str(x0)+" es un valor aproximado a una raiz con un error de "+str(tol))
    elif(dfx == 0):
        print(str(x1)+ " es una posible raiz multiple")
    else:
        print("fracaso en "+str(itera)+" iteraciones")

        
def main():
    x0 = input("x0\n")
    tol = input("tolerancia\n")
    ite = input("iteraciones\n")
    f = lambda x: math.exp(-x**2+5) + math.log(x**2 + 3) - 4*x + 45
    #f = lambda x: math.exp(-x) - (x**2)*math.cos(2*x-4) + 6*x + 3  #function here
    df = lambda x:   -2*x * math.exp(-x**2+5) + ((2*x)/(x**2+3)) - 4# f'(x)
    newton(f, df, float(x0), float(tol), int(ite))
    
    
main()


