import Code.functions as functions
import math
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

class Faser:


    def __init__(self, config_fn):

        self.config = functions.ReadIni(config_fn)
        self.I = functions.ReadIntens(self.config['datafn'])
        self.support = functions.InitializeSupport(self)
        self.shape = self.I.shape

        # First estimate of object
        G = np.exp(1j*math.pi*2*np.random.rand(*(self.shape)))*np.sqrt(self.I)
        self.g = np.fft.fftshift(np.fft.ifft2(np.fft.fftshift(G))) * self.support
        self.n = 0

    def Get_Projected(self):

        G = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(self.g)))
        G = G * np.sqrt(self.I) / np.abs(G)

        self.gp = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(G)))


    def ER_one_iteration(self):

        self.Get_Projected()
        self.g = self.gp * self.support
        self.n = self.n + 1


    def HIO_one_iteration(self, beta):
        
        self.Get_Projected()
        self.g[self.support] = self.gp[self.support]
        self.g[~self.support] = self.g[~self.support] - beta * self.gp[~self.support]
        self.n = self.n + 1

    def UpdateSupport(self):
        
        u = np.abs(self.g)*self.support
        std = np.std(u)
        u = filters.gaussian_filter(u, self.config['blurr_n'], mode = 'wrap')
        self.support  = u > std*self.config['support_thresh'] 
