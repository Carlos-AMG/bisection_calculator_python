from termcolor import colored
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import *

# Definamos constantes
MAXITER = 50 #cantidad maxima de iteraciones

# Funcion fija probablemente podamos hacerla variable

def f(x):
    return np.exp(-1 * x) - np.cos(3 * x) - 0.5

# Hacemos el plot

def plot(funcion, a, b, tolerancia):
    '''Esta funcion tomara la funcion que queramos evaluar, con los intervalos y el nivel de tolerancia y 
    lo graficara usando matplotlib, mientras grafica nos ira imprimiendo la tabla con las iteraciones'''
    x = np.arange(a-0.5,b+0.5,0.00001)
    y = funcion(x)
    funcionA = f(a)
    funcionB = f(b)
    funcionC = None
    plt.plot(x,y, linewidth=3)
    plt.axhline(y=0, c='black',linewidth=1)
    
    if funcionA * funcionB > 0:
        print(colored(f'NO se puede aplicar el metodo de biseccion, {a} y {b} tienen el mismo simbolo', "red"))
        exit()
    print("\t\t\tTabla de iteraciones")
    print('--------------------------------------------------------------------------')
    print('iter \t a \t\t b \t\t c \t\t f(c)        ')
    print('--------------------------------------------------------------------------')

    for iteracion in range(MAXITER):
        c = (a + b)/2
        plt.title(r"$\bf{ITERATION} $ #"+str(iteracion+1)+'\n\na = % 10.8f;       b = % 10.8f;      c = ?;       f(c) = ?'%(a, b))
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.rcParams.update({'font.size': 16})
        axis = plt.gca()

        funcionA = f(a)
        funcionB = f(b)
        funcionC = f(c)

        second_axis = axis.secondary_xaxis("top")
        etiquetas = [item.get_text() for item in second_axis.get_xticklabels()]
        ticks = plt.xticks()[0]
        etiquetas = ["a", "b"]
        second_axis.set_xticks([a, b])
        second_axis.set_xticklabels(etiquetas)
        plt.scatter(a, f(a), c="blue", s=250,alpha=0.5)
        plt.scatter(b, f(b), c="blue", s=250,alpha=0.5)
        plt.annotate("f(a)", [a, f(a)])
        plt.annotate("f(b)", [b, f(b)])
        plt.axvline(x=a, c='blue',linewidth=2,alpha=0.5)
        plt.axvline(x=b, c='blue',linewidth=2,alpha=0.5)

        plt.pause(1)
        plt.rcParams.update({'font.size': 16})
        plt.title(r"$\bf{ITERATION} $ #" + str(iteracion+1) + '\n\na = % 10.8f;       b = % 10.8f;      c = % 10.8f;       f(c) = % 10.8f'%(a, b, c, f(c)))
        plt.rcParams.update({'font.size': 16})
        plt.annotate('f(c)',[c, f(c)])
        etiquetas = [item.get_text() for item in second_axis.get_xticklabels()]
        ticks = plt.xticks()[0]
        etiquetas = ["a", "b", "c=(a+b)/2"]
        second_axis.set_xticks([a,b,c])
        second_axis.set_xticklabels(etiquetas)

        plt.scatter(c, f(c), c="red", s=250, alpha=0.5)
        plt.axvline(x=c, c="red", linewidth=2, alpha=0.5)
        plt.autoscale()

        # Impresion a la tabla en la CLI
        print(str(iteracion+1)+"\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t"%(a,b,c,funcionC))
        plt.pause(1.0)
        
        # Verificar que la raiz este entre a y c, si no entonces esta entre b y c
        if ():
            # Cambiamos el lower bound
            pass





    plt.show()

        



def main():
    print(colored('\tCalculadora de metodo de biseccion', 'cyan'))
    a = float(input("Ingrese el intervalo a: "))
    b = float(input("Ingrese el intervalo b: "))
    tolerancia = float(input("Ingrese el nivel de tolerancia: "))
    print(a,b)
    plot(f, a, b, tolerancia)

# return np.exp(-1 * x) - np.cos(3 * x) - 0.5

if __name__ == "__main__":
    main()