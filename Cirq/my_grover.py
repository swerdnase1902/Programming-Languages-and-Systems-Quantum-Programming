import cirq
import numpy as np
import matplotlib

print(cirq.google.Bristlecone)


class OracleGate(cirq.Gate):
    def __init__(self, n, Z, name):
        super(OracleGate, self)
        self.n = n
        self.Z = Z
        self.name = name

    def _num_qubits_(self):
        return self.n

    def _unitary_(self):
        return self.Z

    def __str__(self):
        return self.name

    # def _circuit_diagram_info_(self, args):
    #     return self.name


def make_oracle(n, f):
    # produces Z_f, in np.array
    diag = [(-1) ** f(i) for i in range(2 ** n)]
    Z_f = np.diag(diag)
    return Z_f


def make_grover_curcuit(n, Z_f):
    Z_0 = np.eye(2**n)
    Z_0[0, 0] = -1
    qubits = cirq.LineQubit.range(n)

    Z_0_gate = OracleGate(n, Z_0, 'Z_0')
    Z_f_gate = OracleGate(n, Z_f, 'Z_f')

    ops = [cirq.H(q) for q in qubits] + [Z_f_gate.on(*qubits)] + [cirq.H(q) for q in qubits] + [Z_0_gate.on(*qubits)] + [cirq.H(q) for q in
                                                                                                 qubits] + [cirq.measure(*qubits, key='result')]
    grover_circuit = cirq.Circuit(ops)
    return grover_circuit
    print(grover_circuit)


if __name__ == '__main__':
    def f1(x):
        if x == 0b00:
            return 1
        else:
            return 0


    Z_f1 = make_oracle(2, f1)
    grover_f1 = make_grover_curcuit(2, Z_f1)
    simulator = cirq.Simulator()
    result = simulator.run(grover_f1)
    print('Measurement results')
    print(result.histogram(key='result'))

    def f2(x):
        if x == 0b00101:
            return 1
        else:
            return 0


    Z_f2 = make_oracle(5, f2)
    grover_f2 = make_grover_curcuit(5, Z_f2)
    simulator = cirq.Simulator()
    result = simulator.run(grover_f2, repetitions=1000)
    print('Measurement results')
    print(result.histogram(key='result'))

    def f3(x):
        if x == 0b0010100:
            return 1
        else:
            return 0


    Z_f3 = make_oracle(7, f3)
    grover_f3 = make_grover_curcuit(7, Z_f3)
    simulator = cirq.Simulator()
    result = simulator.run(grover_f3, repetitions=10000)
    print('Measurement results')
    print(result.histogram(key='result'))
