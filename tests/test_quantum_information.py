import pytest

from qc.quantum_information import *


def test_von_neumann_entropy():
    rho = np.matrix([[1, 0], [0, 0]])
    assert von_neumann_entropy(rho) == 0

    rho = np.matrix([[1, 1], [1, 1]]) / 2
    assert von_neumann_entropy(rho) == pytest.approx(0)

    rho = np.matrix([[2, 1], [1, 1]]) / 3
    assert von_neumann_entropy(rho) == pytest.approx(0.5500477595827574)
