import numpy as np
from .processes import GBM
from .stats import summary
from .black_scholes import call_price

class MonteCarloPricer:
    def __init__(self, S0, r, sigma, T, paths, seed=0):
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.paths = paths
        self.rng = np.random.default_rng(seed)

    def price(self, payoff, antithetic=False, control_variate=False):
        Z = self.rng.standard_normal(self.paths)

        if antithetic:
            Z = np.concatenate([Z, -Z])

        ST = GBM(self.r, self.sigma).simulate(self.S0, self.T, Z)
        payoffs = payoff(ST)
        discounted = np.exp(-self.r * self.T) * payoffs

        if control_variate:
            bs = call_price(self.S0, payoff.K, self.r, self.sigma, self.T)
            control = discounted
            b = np.cov(discounted, control)[0, 1] / np.var(control)
            discounted = discounted - b * (control - bs)

        return summary(discounted)
