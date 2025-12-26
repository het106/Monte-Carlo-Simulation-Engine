import numpy as np

class GBM:
    def __init__(self, r, sigma):
        self.r = r
        self.sigma = sigma

    def simulate(self, S0, T, Z):
        return S0 * np.exp(
            (self.r - 0.5 * self.sigma**2) * T +
            self.sigma * np.sqrt(T) * Z
        )
