from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator


def hadamard(circuit: QuantumCircuit, qubits: int):
    """
    Put all qubits in a superposition
    """
    for qubit in range(qubits):
        circuit.h(qubit)


def simulate(circuit, shots=1000):
    aer_sim = AerSimulator()
    transpiled_circuit = transpile(circuit, aer_sim)
    job = aer_sim.run(transpiled_circuit, shots=shots)  # run the experiment
    result = job.result()  # get the results
    # interpret the results as a "counts" dictionary
    return result.get_counts()


def measure(circuit, nqubits: int):
    """
    Measure the first nqubits
    """
    for i in range(nqubits):
        circuit.measure(i, i)
