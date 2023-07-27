from qc.information import *
import pytest

def test_kolmogorov_distance():
    p = [1., 0.]
    q = [0.5, 0.5]
    assert kolmogorov_distance(p, q) == 1. / 2

    p = [1./2, 1./3, 1./6]
    q = [3./4, 1./8, 1./8]
    assert kolmogorov_distance(p, q) == 1. / 4


def test_fidelity():
    p = [1., 0.]
    q = [0.5, 0.5]
    assert fidelity(p, q) == pytest.approx(0.7071067811865475)

    p = [1./2, 1./3, 1./6]
    q = [3./4, 1./8, 1./8]
    assert fidelity(p, q) == pytest.approx(0.9608341482251325)
