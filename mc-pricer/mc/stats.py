import numpy as np

def summary(x):
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    stderr = std / np.sqrt(n)
    ci_low = mean - 1.96 * stderr
    ci_high = mean + 1.96 * stderr
    return mean, n, std, stderr, (ci_low, ci_high)
