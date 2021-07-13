import pytest

from qc.gates import *
from qc.vectors import *


def test_vector_outer_product():
    x = vector([2, 3])
    y = vector([4, 6, 3])
    t = outer_product(x, y)
    assert "[ 8 12  6 12 18  9]" == str(t.ravel())


def test_bits_to_vector():
    v = bits_to_vector("011")
    assert 3 == bits_to_int("011")
    assert "[0 0 0 1 0 0 0 0]" == str(v)
    v = bits_to_vector("111")
    assert 7 == bits_to_int("111")
    assert "[0 0 0 0 0 0 0 1]" == str(v)


def test_state_from_bloch():
    theta = np.pi / 4
    phi = np.pi / 4
    s = state_from_bloch(theta, phi)
    assert "[0.70710678+0.j  0.5       +0.5j]" == str(s)


def test_gate_outer_product():
    product = outer_product(NOT, identity(2))
    assert ('[[0. 0. 1. 0.]\n' \
            ' [0. 0. 0. 1.]\n' \
            ' [1. 0. 0. 0.]\n' \
            ' [0. 1. 0. 0.]]'
            == str(product))


def test_create_bell_state():
    """
    Build a bell state by applying two sets of gates to a 2-bit system
    :return:
    """
    gate1 = outer_product(hadamard(), identity(2))
    gate2 = CNOT
    input = bits_to_vector("00")
    output1 = gate1 @ input
    output2 = gate2 @ output1
    assert 0.70710678 == pytest.approx(output2[0])
    assert 0 == output2[1]
    assert 0 == output2[2]
    assert 0.70710678 == pytest.approx(output2[3])
