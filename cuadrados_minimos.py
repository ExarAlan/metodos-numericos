import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Trabajo Practico de Metodos Numericos\n")
print("Cuadrados Mínimos y Correlacion Lineal\n")
print("Integrantes\n")
print("Alan Exarchos, DNI 42291365, mail: alanexarchos@gmail.com\n")
print("Marcelo Sanchez, DNI 42629401, mail: smarce18g@gmail.com\n")

# Cargar datos desde un archivo de Excel
df = pd.read_excel('ACUMULADOS_vs_DIAS.xlsx',sheet_name='Hoja1', skiprows=4, usecols="C:D")
df = df.dropna()
# Obtener los datos de acumulación de infectados
dias = df['día'].values
acumulados = df['acumulados'].values

# Cuadrados mínimos - Curva y = ax + b

A = np.vstack([dias, np.ones(len(dias))]).T
a, b = np.linalg.lstsq(A, acumulados, rcond=None)[0]
y_linear = a * dias + b

# Coeficiente de correlación r - Curva y = ax + b
correlacion_linear = np.corrcoef(acumulados, y_linear)[0, 1]

# Cuadrados mínimos - Curva y = b * x^a
log_acumulados = np.log(acumulados)
log_A = np.vstack([np.log(dias), np.ones(len(dias))]).T
log_a, log_b = np.linalg.lstsq(log_A, log_acumulados, rcond=None)[0]
y_potencial = np.exp(log_b) * (dias ** log_a)

# Coeficiente de correlación r - Curva y = b * x^a
correlacion_potencial = np.corrcoef(acumulados, y_potencial)[0, 1]

# Cuadrados mínimos - Curva y = b * e^(ax)
exp_A = np.vstack([dias, np.ones(len(dias))]).T
exp_a, exp_b = np.linalg.lstsq(exp_A, np.log(acumulados), rcond=None)[0]
y_exponencial = np.exp(exp_b) * np.exp(exp_a * dias)

# Coeficiente de correlación r - Curva y = b * e^(ax)
correlacion_exponencial = np.corrcoef(acumulados, y_exponencial)[0, 1]

# Gráfico de los datos y las curvas de tendencia
plt.figure(figsize=(12, 8))
plt.scatter(dias, acumulados, color='blue', label='Datos')
plt.plot(dias, y_linear, color='red', label=f'y = {a:.2f}x + {b:.2f}, r = {correlacion_linear:.2f}')
plt.plot(dias, y_potencial, color='green', label=f'y = {np.exp(log_b):.2f}x^{log_a:.2f}, r = {correlacion_potencial:.2f}')
plt.plot(dias, y_exponencial, color='orange', label=f'y = {np.exp(exp_b):.2f}e^{exp_a:.2f}x, r = {correlacion_exponencial:.2f}')
plt.xlabel('Días')
plt.ylabel('Acumulados')
plt.title('Datos y Curvas de Tendencia')
plt.legend()
plt.grid(True)
plt.show()

# Cálculo de las derivadas numéricas
primera_derivada = np.gradient(acumulados, dias)
segunda_derivada = np.gradient(primera_derivada, dias)

# Gráfico de la primera derivada
plt.figure(figsize=(12, 6))
plt.plot(dias, primera_derivada, color='blue', label='Primera Derivada')
plt.xlabel('Días')
plt.ylabel('Valor')
plt.title('Primera Derivada')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de la segunda derivada
plt.figure(figsize=(12, 6))
plt.plot(dias, segunda_derivada, color='red', label='Segunda Derivada')
plt.xlabel('Días')
plt.ylabel('Valor')
plt.title('Segunda Derivada')
plt.legend()
plt.grid(True)
plt.show()
    
# Cálculo del tiempo de duplicación

tiempo_duplicacion = np.log(2) / exp_a

# Imprimir resultados
print(f"Coeficiente de correlación (y = ax + b): {correlacion_linear:.4f}")
print(f"Coeficiente de correlación (y = b * x^a): {correlacion_potencial:.4f}")
print(f"Coeficiente de correlación (y = b * e^(ax)): {correlacion_exponencial:.4f}")
print(f"Tiempo de duplicación: {tiempo_duplicacion:.2f} días")
print("En el análisis realizado, se ajustaron tres curvas a los datos de acumulación de individuos infectados a lo largo de los días.\n") 
print("Las curvas propuestas fueron y = ax + b, y = b * xa y y = b * e^(ax). \n")
print("La curva y = b * xa mostro el mejor ajuste, con un coeficiente de correlación 0.9786. Esto sugiere un comportamiento potencial en la acumulación de infectados.\n")
print("Los gráficos de las derivadas nos permiten visualizar la tasa de cambio de la acumulación de infectados. \n")
print("La primera derivada muestra la velocidad a la que aumenta o disminuye el número de infectados, mientras que la segunda derivada muestra la aceleración o desaceleración del crecimiento.\n")  
print("El tiempo de duplicación estimado fue de 12.85 días. Esto significa que, en promedio, el número de infectados se duplica aproximadamente cada 12.85 días.")
