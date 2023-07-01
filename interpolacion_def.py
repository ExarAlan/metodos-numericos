import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from numpy import random

print("Trabajo Practico de Metodos Numericos\n")
print("Interpolacion\n")
print("Integrantes\n")
print("Alan Exarchos, DNI 42291365, mail: alanexarchos@gmail.com\n")
print("Marcelo Sanchez, DNI 42629401, mail: smarce18g@gmail.com\n")
 
# interpolacion de newton con Diferencias Finitas 
def interpolacion_newton(xi,fi):
    n = len(xi)
    ki = np.arange(0,n,1)

    tabla = np.concatenate(([ki],[xi],[fi]), axis = 0)
    tabla = np.transpose(tabla)
    dfinita = np.zeros((n,n), dtype=float)
    tabla = np.concatenate((tabla,dfinita), axis=1)

    [n,m] = np.shape(tabla)
    j = 3
    diagonal = n-1
    while(j<m):
        i = 0
        while(i<diagonal):
            tabla[i,j] = tabla[i+1,j-1] - tabla[i,j-1]
            i = i+1
        j = j+1
        diagonal -=1

    n = len(xi)
    x = sym.Symbol('x')
    dfinita = tabla[0,3:]
    h = xi[1]-xi[0]
    polinomio = fi[0]

    for j in range(0,n,1):  
        denominador = np.math.factorial(j) * (h**j)
        factor = dfinita[j-1]/denominador
        termino = 1
        for k in range(0,j,1):
                termino = termino*(x-xi[k])
        polinomio+=termino*factor
    polinomiosimple = sym.expand(polinomio)
    px = sym.lambdify(x,polinomiosimple)

    a = np.min(xi)
    b = np.max(xi)
    p_xi = np.linspace(a,b,50)
    pxi = px(p_xi)
    print("grado del polinomio ", len(xi)-1,"\n")
    print("polinomio", polinomio ,"\n")
    print("polinomio simple", polinomiosimple,"\n")

    plt.scatter(xi, fi, color="yellow" , edgecolor="blue" , label="puntos", zorder = 2)
    plt.plot(p_xi,pxi,color="blue",label='polinomio', zorder = 1)
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Diferencia Finita')
    plt.show()

num_elementos = 20

cota_minima, cota_maxima = 10,100
rango_inicial = random.randint(cota_minima)
rango_final = random.randint(cota_maxima)

# interpolacion normal

x = np.sort(np.linspace(rango_inicial, rango_final, num_elementos))
y = np.random.uniform(rango_inicial, rango_final, num_elementos)

interpolacion_newton(x,y)

#interpolaicon inversa
x_inverso = np.flip(x)

interpolacion_newton(x_inverso,y)

print("Al utilzar el orden inverso el resultado es un polinomio diferente dado que cambiar el orden de los puntos altera el orden de los puntos\n ")
print("El grado de las funciones es el mismo dado que depende de la cantidad de pares a interpolar siendo n-1\n")
#interpolacion desordenado 

desorden = np.random.permutation(num_elementos)
x_desordenado = x[desorden]

interpolacion_newton(x_desordenado,y)

print("Al utilzar el orden desordenado no se puede graficar porque no se cumple la equidistancia del eje x \n ")

# interpolacion por metodo de diferencias divididas

def diferencias_divididas(x, y):
    n = len(x)
    coeficientes = np.zeros((n, n))
    coeficientes[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coeficientes[i][j] = (coeficientes[i+1][j-1] - coeficientes[i][j-1]) / (x[i+j] - x[i])
    return coeficientes[0]

def polinomio_interpolador(x, x_values, coefficients):
    n = len(x_values)
    result = 0

    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term
    return result

coeficientes_divididos = diferencias_divididas(x, y)

grado = len(coeficientes_divididos) - 1

print("Grado del polinomio interpolador por Newton:", grado ,"\n")
print("coeficientes_divididos normal ", coeficientes_divididos,"\n")

# Generar puntos para evaluar el polinomio interpolador
x_grafico = np.linspace(cota_minima, cota_maxima, 100)
y_grafico = polinomio_interpolador(x_grafico, x, coeficientes_divididos)

# Imprimir el polinomio interpolador

print(f"Polinomio interpolador normal: {np.poly1d(coeficientes_divididos)} \n")

plt.scatter(x, y, color="yellow" , edgecolor="blue" , label="puntos", zorder = 2)
plt.plot(x_grafico,y_grafico,color="blue",label='polinomio', zorder = 1)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('diferencias_divididas')
plt.show()

print("Podemos sacar como conclusiones que el metodo de cocientes divididos es mas preciso ademas de que no requiere puntos equidistantes \n")