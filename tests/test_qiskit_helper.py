import pytest

from qc.qiskit_helper import *

def test_hadamard():
    qc = QuantumCircuit(2,2)
    # Apply Hadamard gates before querying the oracle
    hadamard(qc, 2)
    measure(qc, 2)
    results = simulate(qc, 100)
    print(results)
    assert len(results) == 4