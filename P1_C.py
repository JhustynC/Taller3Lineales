import numpy as np
import matplotlib.pyplot as plt

def dibujar_armonicos_y_suma(n=4, p=np.pi):
    t = np.linspace(0, 2*p, 1000)  # Vector de tiempo
    suma_armonicos = np.zeros_like(t)  # Inicializar la suma de los armónicos

    plt.figure()
    for k in range(1, n+1):
        y_k = np.cos(k * np.pi * t)
        plt.plot(t, y_k, label=f'y_k, k = {k}')
        suma_armonicos += y_k
    
    # Dibujar la función suma
    plt.plot(t, suma_armonicos, 'k', linewidth=2, label='Suma de armónicos')
    
    plt.title('Armonicos y_k = cos(kπt) y su suma')
    plt.xlabel('t')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.show()

# Ejecutar la función
dibujar_armonicos_y_suma(4, np.pi)
