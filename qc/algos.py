from qc.gates import *
from qc.vectors import *


def build_deutsch_oracle(f):
    Uf = np.zeros(shape=(4, 4), dtype=int)
    if f(0) == 0:
        Uf[0, 0] = 1
        Uf[1, 1] = 1
    else:
        Uf[0, 1] = 1
        Uf[1, 0] = 1
    if f(1) == 0:
        Uf[2, 2] = 1
        Uf[3, 3] = 1
    else:
        Uf[2, 3] = 1
        Uf[3, 2] = 1
    return Uf


def deutsch(f):
    phi_0 = bits_to_vector("01")
    H = hadamard()
    U1 = outer_product(H, H)
    phi_1 = U1 @ phi_0
    print(f'phi_1 = {phi_1}')
    Uf = build_deutsch_oracle(f)
    phi_2 = Uf @ phi_1
    print(f'phi_2 = {phi_2}')
    U2 = outer_product(H, identity(2))
    phi_3 = U2 @ phi_2
    print(f'phi_3 = {phi_3}')
    if phi_3[0] == 0 and phi_3[1] == 0:
        return 'BALANCED'
    if phi_3[2] == 0 and phi_3[3] == 0:
        return 'CONSTANT'
    raise ValueError("Algorithm failed!")
