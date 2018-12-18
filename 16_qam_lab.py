from scipy import signal
import numpy as np
import time
import RPi.GPIO as GPIO
#import matplotlib.pyplot as plt

t = np.linspace(0, 1, 5000)
#t2 = np.linspace(0, 3, 15000)
x = np.linspace(-np.pi, np.pi, 5000)
r = [0.33, 0.75, 0.75, 1, 0.33, 0.75, 0.75, 1, 0.33, 0.75, 0.75, 1, 0.33, 0.75, 0.75, 1]
p = [225, 255, 195, 225, 135, 105, 165, 135, 315, 285, 345, 315, 45, 75, 15, 45]
#   0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
p_rad = []

for i in range(16):
    p_rad.append((p[i]/180)*np.pi)



serra = signal.sawtooth(2 * np.pi * 1500* t)

sinais = []

for i in range (16):
    sinais.append(r[i]*np.sin(30*x + p[i]))


pwm = []



for j in range (16):
    for i in range(5000):
        if sinais[j][i] >= serra[i]:
            pwm.append(0)
        else:
            pwm.append(1)


GPIO.setmode(GPIO.BOARD)   #Configura o modo de definição de pinos como BOARD (contagem de pinos da placa)

GPIO.setwarnings(False)           #Desativa os avisos

GPIO.setup(8, GPIO.OUT)       #Configura o pino 18 da placa (GPIO24) como saída



while(1):

    for i in range(80000):

        GPIO.output(8, pwm[i])
        time.sleep(0.0005)
        

    