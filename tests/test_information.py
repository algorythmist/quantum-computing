import pytest

from qc.information import *


def test_kolmogorov_distance():
    p = [1., 0.]
    q = [0.5, 0.5]
    assert kolmogorov_distance(p, q) == 1. / 2

    p = [1. / 2, 1. / 3, 1. / 6]
    q = [3. / 4, 1. / 8, 1. / 8]
    assert kolmogorov_distance(p, q) == 1. / 4


def test_fidelity():
    p = [1., 0.]
    q = [0.5, 0.5]
    assert fidelity(p, q) == pytest.approx(0.7071067811865475)

    p = [1. / 2, 1. / 3, 1. / 6]
    q = [3. / 4, 1. / 8, 1. / 8]
    assert fidelity(p, q) == pytest.approx(0.9608341482251325)


def test_shannon_entropy():
    fair_coin = [1. / 2, 1. / 2]
    assert shannon_entropy(fair_coin) == 1.
    fair_die = np.ones(6) / 6
    assert shannon_entropy(fair_die) == pytest.approx(2.584962500721156)
    biased_coin = [0.6, 0.4]
    assert shannon_entropy(biased_coin) == pytest.approx(0.9709505944546686)
    biased_die = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
    assert shannon_entropy(biased_die) == pytest.approx(2.1609640474436813)
