import pytest
from qc.complex import normalize, norm


def test_norm():
    assert 1.4142135623730951 == norm([1, 1])
    assert 3.0 == pytest.approx(norm([1 + 1j, 2 - 1j, 1 - 1j]))


def test_normalize():
    n = normalize([1, 1])
    print(n)
    assert n.tolist() == [0.7071067811865475, 0.7071067811865475]
    assert 1.0 == pytest.approx(norm(n))

    n = normalize([1 + 1j, 2 - 1j, 1 - 1j])
    assert n.tolist() == [(0.33333333333333326 + 0.33333333333333326j), (0.6666666666666665 - 0.33333333333333326j),
                          (0.33333333333333326 - 0.33333333333333326j)]

    assert 1.0 == pytest.approx(norm(n))
