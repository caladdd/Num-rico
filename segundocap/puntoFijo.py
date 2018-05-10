import math

def puntofijo(f, g, h, i, x0, tol, itera):
    fx=f(x0)
    cont=0
    print("xn "+str(x0)+ " fnx "+ str(fx)+ " f'nx "+ str(h(x0))+ " f''nx "+ str(i(x0)))
    error=tol+1
    while((fx!=0) and (error > tol) and (cont<itera)):
        xn = x0 - ((f(x0)*h(x0))/(h(x0)**2-(f(x0)*i(x0))))
        fx = f(xn)
        error = abs((xn - x0))
        print("xn "+str(xn)+ " fnx "+ str(fx)+ " f'nx "+ str(h(xn))+ " f''nx "+ str(i(xn))+ " err "+str(error))
        cont = cont + 1
        x0 = xn

    if(fx == 0):
        print(str(x0)+" es la raiz")
    elif(error<tol):
        print(str(x0)+" es un valor aproximado a una raiz con un error de "+str(tol))
    else:
        print("fracaso en "+str(itera)+" iteraciones")

        
def main():
    x0 = input("x0\n")
    tol = input("tolerancia\n")
    ite = input("iteraciones\n")
    f = lambda x: math.exp(-6*x) - 12*x**2 * math.exp(-3*x) - 36*x**4  #function here
    h = lambda x: -6 * math.exp(-6*x) - (12*x**2 * (-3* math.exp(-3*x)) + math.exp(-3*x) * 24*x) - 144*x**3 
    i = lambda x: 36 * math.exp(-6*x) - ((12*x**2 * (9 * math.exp(-3*x)) + 24*x * (-3* math.exp(-3*x))) + ((math.exp(-3*x) * 24) + (-3 * math.exp(-3*x) * 24*x))) - 432*x**2 
    g = lambda x: x - ((math.exp(-3*x) - 6 * x**2)/(-3 * math.exp(-3*x) - 12 * x)) + ((9 * math.exp(-3*x) - 12)/2*(-3 * math.exp(-3*x) - 12 * x))*((math.exp(-3*x) - 6 * x**2)/(-3 * math.exp(-3*x) - 12 * x))**2  #function here
    puntofijo(f, g, h, i, float(x0), float(tol), int(ite))
    
    
main()
