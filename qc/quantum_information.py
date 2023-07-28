import numpy as np
from scipy import linalg as la


def von_neumann_entropy(rho):
    """
    Compute the von Neumann entropy of a density matrix
    :param rho: the density matrix
    :return: the von Neumann entropy
    """
    assert rho.shape[0] == rho.shape[1]
    # compute eigenvalues
    eigenvalues, _ = la.eig(rho)
    # remove imaginary part since a real density matrix has only real eigenvalues
    eigenvalues = np.real(eigenvalues)
    # remove zero eigenvalues because 0*log(0) = 0
    eigenvalues = eigenvalues[eigenvalues != 0]
    return -np.sum(eigenvalues * np.log2(eigenvalues))


