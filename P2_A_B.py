
import numpy as np
import matplotlib.pyplot as plt

def onda_cuadrada(n, t):
    suma = np.zeros_like(t)
    for k in range(1, n+1):
        armonico = np.sin((2*k - 1) * t) / (2*k - 1)
        suma += armonico
    return suma

# Valores iniciales
n_max = 5
t = np.linspace(-np.pi, np.pi, 1000)

plt.figure()
for n in range(1, n_max + 1):
    y = onda_cuadrada(n, t)
    plt.plot(t, y, label=f'n = {n}')
    
plt.title('Aproximación de una onda cuadrada mediante suma de armónicos')
plt.xlabel('t')
plt.ylabel('Suma de armónicos')
plt.legend()
plt.grid(True)
plt.show()
