import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros de la simulación
R_base = 1  # Resistencia base (cuando el nadador está alineado)
k = 0.05     # Factor de incremento de resistencia por el ángulo
theta = np.linspace(0, 5, 15)  # Ángulos de inclinación de 0 a 45 grados

# Convertir el ángulo a radianes
theta_radianes = np.radians(theta)

# Calcular la resistencia en función del ángulo
R = R_base * (1 + k * theta_radianes**2)

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(theta, R, label='Resistencia (arrastre)', color='b')
plt.title('Simulación de Resistencia vs Ángulo de Inclinación del Nadador')
plt.xlabel('Ángulo de Inclinación (grados)')
plt.ylabel('Resistencia (arrastre)')
plt.grid(True)
plt.legend()
plt.show()
