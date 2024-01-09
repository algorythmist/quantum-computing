from sympy import *
from sympy.physics import msigma


def calc_bloch_transform(E):
    """
    Wayne Dam
    :param E:list of the E_i Kraus operators for the operator sum representation.
    :return: M,c: Matrix and vector of the affine map r -> r' = Mr + c (equation 8.89)
    """
    P = len(E)
    M = zeros(3)

    a = [[Trace(E[i].H * msigma(k) / 2).simplify() for k in [1, 2, 3]] for i in range(P)]
    alpha = [Trace(E[i].H).simplify() / 2 for i in range(P)]
    # Addressing a ~ [number of E_i's, 3]
    # Addressing alpha ~ [number of E_i's]

    for j in range(3):
        for k in range(3):
            M[j, k] = sum([
                a[l][j] * conjugate(a[l][k]) + conjugate(a[l][j]) * a[l][k] +
                (
                        abs(alpha[l]) ** 2.0 -
                        sum([a[l][p] * conjugate(a[l][p]) for p in range(3)])
                ) * KroneckerDelta(j, k) +
                I * sum([
                    LeviCivita(j, k, p) * (alpha[l] * conjugate(a[l][p] - conjugate(alpha[l] * a[l][p]))) for p in
                    range(3)
                ])
                for l in range(P)
            ])

    c = zeros(3, 1)
    for k in range(2):
        c[k] = 2 * I * sum([LeviCivita(j, p, k) * a[l][j] * conjugate(a[l][p])
                            for l in range(P) for j in range(3) for p in range(3)])

    return M, c