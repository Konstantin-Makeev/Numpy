import numpy as np
from numpy import linalg

vec1 = np.random.normal(size=100)
vec2 = np.random.poisson(lam=10, size=100)
print(linalg.norm(vec1 - vec2))
