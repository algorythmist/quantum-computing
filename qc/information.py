import numpy as np


def kolmogorov_distance(p, q):
    """
    Compute the Kolmogorov distance between two probability distributions
    :param p: the first probability distribution
    :param q: the second probability distribution
    :return: the Kolmogorov distance
    """
    assert len(p) == len(q)
    return np.max(np.abs(np.cumsum(p) - np.cumsum(q)))


def fidelity(p, q):
    """
    Compute the fidelity between two probability distributions
    :param p: the first probability distribution
    :param q: the second probability distribution
    :return: the fidelity
    """
    assert len(p) == len(q)
    return np.dot(np.sqrt(p), np.sqrt(q))
