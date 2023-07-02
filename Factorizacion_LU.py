import numpy as np
import scipy.linalg

def numero_operaciones_elemantales(n):
    # Calculamos el numero de operaciones elementales 
  
    numero_operaciones = (n**2)/2  ## Ly = b
    numero_operaciones_atras = n*(n+1)/2   ## Ux = y
    total_operaciones = numero_operaciones + numero_operaciones_atras
    return numero_operaciones, numero_operaciones_atras, total_operaciones

def determinante_distinto_de_cero(matrix):
    # Verificamos el determinante de la matriz
    det = np.linalg.det(matrix)

    # Tambien el de las submatrices
    if det != 0:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                submatrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                if np.linalg.det(submatrix) == 0:
                    return False
        return True
    return False

def ingresar_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = int(input(f"Ingrese el elemento ({i}, {j}) de la matriz: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz


def ingreso_vector_B(n):
    vector_b = []
    for i in range(n):
        temp = int(input(f"Ingrese el valor {i} del vector B: "))
        vector_b.append(temp)

    return vector_b

def mostrar_datos(a, b):
    print("Matriz: ")
    print(a)
    print("\n")

    print("Vector B: ")
    print(b)
    print("\n")

def descomposicion_LU(A):
    return scipy.linalg.lu(A)

# Matriz y vector B de ejemplo
# A = np.array([[2, -1, 3], [4, 1, 1], [-6, 3, -1]])
# b = np.array([9, 7, -4])

print("Trabajo Practico de Metodos Numericos\n")
print("Factorizacion LU \n")
print("Integrantes\n")
print("Alan Exarchos, DNI 42291365, mail: alanexarchos@gmail.com\n")
print("Marcelo Sanchez, DNI 42629401, mail: smarce18g@gmail.com\n")

print("a)Para calcular la cantidad de operaciones elementales en la ecuacion matricial Ly = b mediante sustitucion hacia adelante, es aproximadamente n^2 / 2, donde n es \n ")
print("el tamaño de la matriz y el vector.Esto se debe a que, en cada iteracion del algoritmo de sustitucion hacia adelante, se realiza una multiplicacion y una resta para calcular la suma parcial \n ")
print("de la ecuacion: (n**2)/2 \n ")

print("b) Para despejar el vector x en la ecuación matricial Ux = y, donde U es una matriz triangular superior, se utiliza el método de sustitución hacia atrás. \n")
print("En cada paso de la sustitución hacia atrás, se calcula el valor de un elemento de x utilizando los valores ya conocidos de x y y.\n")

print("En el peor caso, cada elemento de x debe ser calculado utilizando todos los elementos posteriores de x. \n")
print("Esto implica que, para el elemento x[i], se deben realizar n-i operaciones elementales para calcular su valor.\n")
print("Dado que x tiene n elementos, la cantidad total de operaciones elementales en el peor caso para despejar x es:\n")
print("Operaciones elementales en el peor caso para despejar x = 1 + 2 + 3 + ... + (n-1) + n\n")
print("Podemos utilizar la fórmula de la suma de los primeros n números naturales para simplificar la expresión:\n")
print("Operaciones elementales en el peor caso para despejar x = n * (n + 1) / 2\n")
print("Por lo tanto, en el peor caso, se necesitan n * (n + 1) / 2 operaciones elementales para despejar el vector x en la ecuación matricial Ux = y.\n")

print("c) La cantidad total de operaciones elementales requeridas en el peor caso para las dos etapas del método LU se obtiene sumando las operaciones elementales de ambas etapas.\n")

n = int(input("Ingrese el tamaño de la matriz: "))

A = np.array(ingresar_matriz(n))
b = np.array(ingreso_vector_B(n))

if not determinante_distinto_de_cero:
    raise ValueError("Hay un determinante de la matriz que es 0")

mostrar_datos(A, b)

P, L, U = descomposicion_LU(A)

print("Descomposición LU:")
print(" ")

print("Matriz P:")
print(np.round(P, decimals=3))
print(" ")

print("Matriz L:")
print(np.round(L, decimals=3))
print(" ")

print("Matriz U:")
print(np.round(U, decimals=3))
print(" ")

dimension = len(b)
numero_operaciones, numero_operaciones_atras, total_operaciones = numero_operaciones_elemantales(dimension)

print("Numero total de operaciones elementales Ly=b: \n", numero_operaciones)
print("Numero total de operaciones elementales Ux=y: \n", numero_operaciones_atras)
print("Numero total de operaciones elementales: \n", total_operaciones)
