import numpy as np
import matplotlib.pyplot as plt

def dibujar_armonicos(n=4, p=np.pi):
    t = np.linspace(0, 2*p, 1000)  # Vector de tiempo

    plt.figure()
    for k in range(1, n+1):
        y = np.cos((k * np.pi * t) / p)
        plt.plot(t, y, label=f'k = {k}')
    
    plt.title('Armonicos cos(kπt/p)')
    plt.xlabel('t')
    plt.ylabel('cos(kπt/p)')
    plt.legend()
    plt.show()

# Ejecutar la función
dibujar_armonicos(4, np.pi)
