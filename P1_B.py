import numpy as np
import matplotlib.pyplot as plt

def dibujar_armonicos_con_suma(n=4, p=np.pi):
    t = np.linspace(-2*p, 2*p, 1000)  # Vector de tiempo
    suma_armonicos = np.zeros_like(t)  # Inicializar la suma de los armónicos

    plt.figure()
    for k in range(1, n+1):
        y = np.cos((k * np.pi * t) / p)
        plt.plot(t, y, label=f'k = {k}')
        suma_armonicos += y
    
    # Dibujar la función suma
    plt.plot(t, suma_armonicos, 'k', linewidth=2, label='Suma de armónicos')
    
    plt.title('Armonicos cos(kπt/p) y su suma')
    plt.xlabel('t')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.show()

# Ejecutar la función
dibujar_armonicos_con_suma(4, np.pi)
