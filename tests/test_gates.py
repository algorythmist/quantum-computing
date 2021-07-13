import pytest

from qc.gates import *
from qc.vectors import *


def test_tofoli():
    t = tofoli()
    u = t @ t
    assert is_unit_matrix(u)


def test_fredkin():
    f = fredkin()
    u = f @ f
    assert is_unit_matrix(u)


def test_bit_inner_product():
    assert 0 == bit_inner_product("000", "000")
    assert 1 == bit_inner_product("01", "01")
    assert 1 == bit_inner_product("111", "111")
    assert 0 == bit_inner_product("110", "111")


def test_into_to_bits():
    assert "0001" == int_to_bits(1, 4)
    assert "011" == int_to_bits(3, 3)


def test_hadamard():
    h = hadamard()
    assert 0.70710678 == pytest.approx(h[0][1])
    assert -0.70710678 == pytest.approx(h[1][1])

    h = hadamard(2)
    assert 0.5 == pytest.approx(h[0][1])
    assert -0.5 == pytest.approx(h[1][1])
