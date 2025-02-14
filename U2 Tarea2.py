#U2T2
import random
import numpy as np
from scipy.stats import kstest

numeros_aleatorios = [random.random() for _ in range(100)]

estadistico, p_value = kstest(numeros_aleatorios, 'uniform')

print(f'Estadístico de Kolmogorov-Smirnov: {estadistico}')
print(f'Valor p: {p_value}')
s
alpha = 0.05
if p_value > alpha:
    print("No se puede rechazar la hipótesis nula: Los datos parecen ser uniformes.")
else:
    print("Se rechaza la hipótesis nula: Los datos no parecen ser uniformes.")
