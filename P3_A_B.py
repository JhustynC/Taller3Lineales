import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x)
def f(x):
    if 0 <= x <= np.pi:
        return x
    elif -np.pi <= x < 0:
        return 0
    else:
        return 0

# Vectorizar la función para que pueda trabajar con arrays de numpy
f_vec = np.vectorize(f)

# Calcular los coeficientes de la serie de Fourier
def fourier_series(x, n_terms):
    a0 = np.pi / 4
    result = a0
    for n in range(1, n_terms + 1):
        bn = (-1)**(n+1) / n
        an = -2 / (np.pi * (2*n - 1)**2)
        result += an * np.cos((2*n - 1) * x) + bn * np.sin(n * x)
        print(f'Coeficiente {n}: {sum(result)}' )
    return result

# Parámetros
x = np.linspace(-np.pi, np.pi, 1000)
n_terms = 10

# Calcular la suma de los primeros 10 armónicos
fourier_sum = fourier_series(x, n_terms)

# Graficar la función original y la suma de la serie de Fourier
plt.figure(figsize=(10, 6))

# Graficar la función original
plt.plot(x, f_vec(x), label='f(x)', color='blue')

# Graficar la suma de la serie de Fourier
plt.plot(x, fourier_sum, label=f'Suma de los primeros {n_terms} armónicos', color='red', linestyle='--')

plt.title('Aproximación de f(x) mediante la suma de Fourier')
plt.xlabel('x')
plt.ylabel('f(x) / Suma de Fourier')
plt.legend()
plt.grid(True)
plt.show()
