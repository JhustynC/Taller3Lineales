import numpy as np

def calcular_suma_armonicos(n, t_valores):
    resultados = []
    for t in t_valores:
        suma = 0
        for k in range(1, n+1):
            suma += np.sin((2*k - 1) * t) / (2*k - 1)
        resultados.append(suma)
    return resultados

# Valores iniciales
n = 10
t_valores = [0, np.pi / 2, -np.pi / 3]

resultados = calcular_suma_armonicos(n, t_valores)
for t, suma in zip(t_valores, resultados):
    print(f'Suma de los primeros {n} armónicos en t = {t}: {suma}')
