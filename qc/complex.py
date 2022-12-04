import numpy as np

def norm(vector):
    """
    Norm of a complex vector
    :param vector:
    :return:
    """
    v = np.array(vector)
    return np.sqrt(sum(np.apply_along_axis(lambda c: abs(c)**2, 0, v)))

def normalize(vector):
    """
    normalize the modulus of a complex vector to 1
    :param vector:
    :return:
    """
    v = np.array(vector)
    return v/norm(v)


