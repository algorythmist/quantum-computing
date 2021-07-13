from qc.moduli import *


def test_gcd():
    assert 3 == gcd(21, 15)
    assert 3 == gcd(9, 15)
    assert 3 == gcd(9, 3)
    assert 1 == gcd(9, 28)


def test_find_comprime():
    coprime = find_coprime(15)
    assert 1 == gcd(coprime, 15)


def test_powers():
    p = powers(2, 15)
    assert '[2, 4, 8, 1, 2, 4, 8, 1, 2, 4, 8, 1, 2]' == str(p)
    p = powers(13, 15)
    assert '[13, 4, 7, 1, 13, 4, 7, 1, 13, 4, 7, 1, 13]' == str(p)


def test_find_period():
    period = find_period(2, 371)
    assert 156 == period
    assert 78 == find_period(24, 371)
