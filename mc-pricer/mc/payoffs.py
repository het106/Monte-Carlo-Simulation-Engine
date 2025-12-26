import numpy as np

class EuropeanCall:
    def __init__(self, K):
        self.K = K

    def __call__(self, ST):
        return np.maximum(ST - self.K, 0)
