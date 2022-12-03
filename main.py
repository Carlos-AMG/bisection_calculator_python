import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from utils import *
from termcolor import colored

# Definamos constantes
MAXITER = 50 #cantidad maxima de iteraciones

global condicion

def al_cerrar(evt=None):
    exit()
# Hacemos el plot

def plot(f, a, b, tolerancia):
    '''Esta funcion tomara la funcion que queramos evaluar, con los intervalos y el nivel de tolerancia y 
    lo graficara usando matplotlib, mientras grafica nos ira imprimiendo la tabla con las iteraciones'''
    plt.figure().canvas.mpl_connect("close_event", al_cerrar)
    # plt.get_current_fig_manager().full_screen_toggle()
    wm = plt.get_current_fig_manager()
    wm.window.state("zoomed")

    x = np.arange(a-0.5,b+0.5,0.00001)
    y = f(x)
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
        plt.title(r"$\bf{ITERACION} $ #"+str(iteracion+1)+'\n\na = % 10.8f;       b = % 10.8f;      c = ?;       f(c) = ?'%(a, b))
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
        plt.scatter(a, funcionA, c="blue", s=250,alpha=0.5)
        plt.scatter(b, funcionB, c="blue", s=250,alpha=0.5)
        plt.annotate("f(a)", [a, funcionA])
        plt.annotate("f(b)", [b, funcionB])
        plt.axvline(x=a, c='blue',linewidth=2,alpha=0.5)
        plt.axvline(x=b, c='blue',linewidth=2,alpha=0.5)

        plt.pause(1) #1
        plt.rcParams.update({'font.size': 16})
        plt.title(r"$\bf{ITERACION} $ #" + str(iteracion+1) + '\n\na = % 10.8f;       b = % 10.8f;      c = % 10.8f;       f(c) = % 10.8f'%(a, b, c, funcionC))
        plt.rcParams.update({'font.size': 16})
        plt.annotate('f(c)',[c, funcionC])
        etiquetas = [item.get_text() for item in second_axis.get_xticklabels()]
        ticks = plt.xticks()[0]
        etiquetas = ["a", "b", "c=(a+b)/2"]
        second_axis.set_xticks([a,b,c])
        second_axis.set_xticklabels(etiquetas)

        plt.scatter(c, funcionC, c="red", s=250, alpha=0.5)
        plt.axvline(x=c, c="red", linewidth=2, alpha=0.5)
        plt.autoscale()

        # Impresion a la tabla en la CLI
        print(str(iteracion + 1) + "\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t" % (a,b,c,funcionC))
        plt.pause(1)#1
        
        # Verificar que la raiz este entre a y c, si no entonces esta entre b y c
        if funcionA * funcionC < 0:
            # Cambiamos el lower bound
            texto = plt.text(0.5, 0.2, 'f(a) * f(c) < 0\n\ncambiamos b = c', fontsize=16,horizontalalignment='center',verticalalignment='center',transform = axis.transAxes)
            texto.set_bbox(dict(facecolor="whitesmoke", alpha=0.5, edgecolor="whitesmoke"))
            plt.scatter(b, funcionA, c="yellow", s=175, alpha=1)
            plt.scatter(b, funcionC, c="yellow", s=175, alpha=1)
            plt.pause(1) #1
            b = c
        else:
            # Cambiamos el lower bound
            a = c
            texto = plt.text(0.5, 0.2, 'f(a) * f(c) < 0\n\ncambiamos b = c', fontsize=16,horizontalalignment='center',verticalalignment='center',transform = axis.transAxes)
            texto.set_bbox(dict(facecolor="whitesmoke", alpha=0.5, edgecolor="whitesmoke"))
            plt.scatter(b, funcionB, c="yellow", s=175, alpha=1)
            plt.scatter(b, funcionC, c="yellow", s=175, alpha=1)

        plt.pause(2) # 2

        # Verificar que la raiz haya sido encontrada en la iteracion actual, con el error aceptable
        # En caso de ser verdad terminamos la funcion

        if np.abs(funcionC) < tolerancia:
            print('--------------------------------------------------------------------------')
            print(colored(f'Raiz encontrada aproximadamente en: {str(c)}', "green"))
            texto.set_bbox(dict(facecolor="papayawhip", alpha=0.06, edgecolor="papayawhip"))
            while True:
                plt.pause(10)
        plt.clf()
        x = np.arange(a - (b - a) / 2, b + (b-a) / 2, 0.00001)
        y = f(x)
        plt.rcParams.update({'font.size': 10})
        plt.plot(x,y, linewidth=3)
        plt.axhline(y=0, c='black',linewidth=1)
    plt.show()
    print('--------------------------------------------------------------------------')
    

def main():
    print(colored('\tCalculadora de metodo de biseccion', 'cyan'))
    expr = input("Ingrese la funcion: ")
    expr = "".join(expr.split())
    for key, value in symbols.items():
        expr = expr.replace(key, value)
    # print(expr)
    f = crear_func(expr)
    a = float(input("Ingrese el intervalo a: "))
    b = float(input("Ingrese el intervalo b: "))
    tolerancia = float(input("Ingrese el nivel de tolerancia: "))
    # print(a,b, f(1.4))
    plot(f, a, b, tolerancia)

# return np.exp(-1 * x) - np.cos(3 * x) - 0.5

if __name__ == "__main__":
    main()