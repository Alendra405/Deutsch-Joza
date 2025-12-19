from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

n = 3

qc = QuantumCircuit(n+1, n)

qc.x(n)
qc.h(range(n+1))
qc.barrier()

qc_constant = qc.copy('constant')
qc_constant.barrier()

qc.cx(0, n)
qc.name = 'balanced'
qc.barrier()

qc.h(range(n))
qc_constant.h(range(n)) 

qc.barrier()
qc_constant.barrier()

qc.measure(range(n), range(n))
qc_constant.measure(range(n), range(n))

backend = AerSimulator()

constant_trans = transpile(qc_constant, backend)
balanced_trans = transpile(qc, backend)

job_constant = backend.run(constant_trans, shots=1024)
job_balanced = backend.run(balanced_trans, shots=1024)

result_constant = job_constant.result()
result_balanced = job_balanced.result()

counts_constant = result_constant.get_counts(qc_constant)
counts_balanced = result_balanced.get_counts(qc)

print("CO:", counts_constant)
print("BA:", counts_balanced)

plot_histogram([counts_constant, counts_balanced], legend=['CO', 'BA'])

plt.show()
