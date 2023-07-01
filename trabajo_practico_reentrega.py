import matplotlib.pyplot as plt
import numpy as np


def secante(x0, x1):
    dfxSecante = (f(x1) - f(x0)) / (x1 - x0)
    xr = x1 - f(x1) / dfxSecante
    return xr


def newton(x0, x1, eps):
    dfxNewton = derivada(x0, eps)
    if abs(dfxNewton) < eps:
        raise ValueError("El denominador se anula.")
    xr = x1 - f(x1) / dfxNewton
    return xr


def derivada(x0, eps):
    return (f(x0 + eps) - f(x0)) / eps


def metodoSecanteNewton(x0, x1, eps=1e-8, maximoIteraciones=1000):
    """
    Combinación del método de la secante con el método de Newton para encontrar alguna raíz real de la función f.

    Args:
        f: función a encontrar su raíz.
        x0: punto inicial para la aproximación de la raíz.
        x1: punto siguiente al punto inicial.
        eps: tolerancia para el criterio de parada.
        maximoIteraciones: número máximo de iteraciones permitidas.

    Returns:
        xr: aproximación de la raíz de la función f con un error menor que eps.
        numeroIteraciones: número de iteraciones realizadas.

    Raises:
        ValueError: si se alcanza el número máximo de iteraciones sin cumplir el criterio de parada.
    """
    print("Trabajo Practico de Metodos Numericos\n")
    print("Integrantes\n")
    print("Alan Exarchos, DNI 42291365, mail: alanexarchos@gmail.com\n")
    print("Marcelo Sanchez, DNI 42629401, mail: smarce18g@gmail.com\n")
    print("Para hallar una raiz de la funcion -> f(x) = x**3 - x - 1\n")
    print(
        "El algoritmo va a intercalar, dependiendo de si el numero de la iteracion es par o impar,"
    )
    print(
        "entre usar el metodo de Newton o el metodo Secante para hallar el proximo X."
    )
    print(
        "Si en esa X que encontró, la funcion es menor al epsilon proporcionado en los argumentos"
    )
    print(
        "entonces va a dejar de iterar. Este es el criterio de parada que elegimos, con precision de 8 decimales."
    )
    print(
        "En caso de que las iteraciones, superen el valor dado en el correspondiente argumento"
    )
    print("se va a levantar un error y tambien va a cortar el bucle.\n")
    print("La funcion que se encarga de realizar el metodo de newton recibe:")
    print("- x0 y x1 que es el intervalo, x0 es el primer valor y x1 el segundo")
    print("- el epsilon que lo vamos a usar para calcular la derivada de la funcion")
    print("Primero va a hallar la derivada de la funcion en el punto x0, luego aplica")
    print("la formula del metodo de newton para hallar el proximo X y lo retorna\n")
    print(
        "De la misma forma que en la funcion que se encarga de Newton, la que se encarga"
    )
    print(
        "del metodo secante, va a aplicar la formula para hallar la siguiente X y la va"
    )
    print("a retornar. En nuestro caso, dividimos la operacion en dos partes.")
    print(
        "Primero calculamos el denominador de la formula y luego en la variable que vamos a retornar"
    )
    print("terminamos de realizar la operacion.\n")

    errores = []
    print("Iteración\tIntervalo\tRaíz aproximada\tF(raiz)\t\tError")
    numeroIteraciones = 1
    while numeroIteraciones < maximoIteraciones:
        if numeroIteraciones % 2 == 0:
            xr = newton(x0, x1, eps)
        else:
            xr = secante(x0, x1)
        fDeRaiz = f(xr)
        error = abs(f(xr))
        print(
            "{}\t,[{:.8f}, {:.8f}], {:.8f}, {:.8f}, {:.8f}".format(
                numeroIteraciones, x0, x1, xr, fDeRaiz, error
            )
        )
        errores.append(abs(f(xr)))
        if abs(f(xr)) < eps:
            return xr, numeroIteraciones, errores
        x0, x1 = x1, xr
        numeroIteraciones += 1
    raise ValueError(
        "El método no converge después de {} iteraciones.".format(maximoIteraciones)
    )


def f(x):
    return x**3 - x - 1


def graficarConvergenciaErrores(errores):
    plt.plot(range(1, len(errores) + 1), errores)
    plt.xlabel("Iteración")
    plt.ylabel("Error")
    plt.title("Convergencia de los errores de las raíces")
    plt.show()


def graficarFuncion():
    x = np.linspace(-3, 3, 400)
    y = f(x)
    plt.plot(x, y, label="f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfico de la funcion: x^3 - x - 1")
    plt.legend()
    plt.grid(True)
    plt.show()

 
a, b = int(input("ingrese el intervalo"))
eps = 1e-8

xr, numeroIteraciones, errores = metodoSecanteNewton(a, b, eps)
print("Raíz aproximada: {:.8f} (en {} iteraciones)".format(xr, numeroIteraciones))
graficarConvergenciaErrores(errores)
graficarFuncion()
