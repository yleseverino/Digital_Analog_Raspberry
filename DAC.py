from scipy import signal
import numpy as np


class DAC:
    """ Iniciando o buffer circular """
    def __init__(self):
        self.PWM = []
        self.serra = []


    def comp(self,x):

        t = np.linspace(0, 1, len(x))

        self.serra = signal.sawtooth(2 * np.pi * 10* t)

        for i in range(len(x)):
            if x[i] >= self.serra[i]:
                self.PWM.append(0)
            else:
                self.PWM.append(1)

    def pegar(self):
        """ retorna os valores do buffer"""
        return self.PWM
