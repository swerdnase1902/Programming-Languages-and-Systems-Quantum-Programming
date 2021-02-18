import cirq
import numpy as np
import matplotlib

print(cirq.google.Bristlecone)


def make_oracle(n, f):
    # produces Z_f, in np.array
    diag = [(-1) ** f(i) for i in range(2 ** n)]
    Z_f = np.diag(diag)
    return Z_f


def grover(n, Z_f):
    Z_0 = np.eye(n)
    Z_0[0, 0] = -1
