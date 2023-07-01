import numpy as np

# A matriz del sistema de ecuaciones
# b vector de valores indepedientes
# x0 vector de variables
# tolerancia
# iteraciones
def jacobi(A, b, x0, tolerancia, iteraciones):
    D = np.diag(np.diag(A))  # diagonal de la matriz
    LU = A - D  # representa L + U
    x = x0  # variable para iniciar el metodo

    for i in range(iteraciones):
        inversaD = np.linalg.inv(D)  # inversa de la diagonal
        xTemp = x  # guarda los valores de la iteracion anterior
        x = np.dot(inversaD, np.dot(-LU, x)) + np.dot(inversaD, b)  # producto entre las matrices
        print("iteracion", i, ": x =", x, "norma", x - xTemp)
        if (np.linalg.norm(x - xTemp) < tolerancia):  # calculo la diferencia entre los vectores , en caso de que sea menor a la tolerancia me salgo del ciclo
            return x
    return x


# ingreso de datos
A = np.array(
    [
        [3, -1, -1],
        [-1, 3, 1],
        [2, 1, 4],
    ]
)
b = [1, 3, 7]
x0 = np.zeros(3)
tolerancia = 1e-4
iteraciones = 500

print("Trabajo Practico de Metodos Numericos\n")
print("Integrantes\n")
print("Alan Exarchos, DNI 42291365, mail: alanexarchos@gmail.com\n")
print("Marcelo Sanchez, DNI 42629401, mail: smarce18g@gmail.com\n")
print(
    "El programa lee la matriz A de numeros reales , el vector solucion B , la cantidad de iteraciones , crea el vector de variables \n"
)
print(
    "Y luego utiliza el metodo de Jacobi para buscar una solucion aproximada al sistema de ecuaciones lineales \n \n 3x - y - z = 1 \n -x + 3y + z = 3 \n 2x + y + 4 = 7 \n"
)
print("Mostrando el vector que resulta en cada paso\n")
print("El programa  se detendra al llegar al maximo de iteraciones , o al tener una diferencia de error entre iteraciones menor al error ingresado \n")

try:
    solucion = jacobi(A, b, x0, tolerancia, iteraciones)
    print("Solucion exacta del sistema de ecuaciones con libreria numPy:")
    print(np.linalg.solve(A, b))
except Exception as e:
    print("Error:", str(e))
