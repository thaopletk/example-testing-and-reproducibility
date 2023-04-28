"""Define a simple stochastic model."""

import numpy as np


def run_model():
    """A simple model that draws samples from a normal distribution."""
    rng = np.random.default_rng()
    values = rng.normal(loc=10, scale=1, size=50)
    return values
