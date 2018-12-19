import DAC
import time
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 500)
x = np.linspace(-np.pi, np.pi, 500)
r = [0.33, 0.75, 0.75, 1, 0.33, 0.75, 0.75, 1, 0.33, 0.75, 0.75, 1, 0.33, 0.75, 0.75, 1]
p = [225, 255, 195, 225, 135, 105, 165, 135, 315, 285, 345, 315, 45, 75, 15, 45]
#   0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
p_rad = []

for i in range(16):
    p_rad.append((p[i]/180)*np.pi)


a = DAC.DAC()

a.comp(0.33*np.sin(1*x + 45))

plt.subplot(2, 1, 1)
plt.plot(t, a.pegar())
plt.subplot(2, 1, 2)
plt.plot(t, 0.33*np.sin(2*x + 45))
plt.show()
