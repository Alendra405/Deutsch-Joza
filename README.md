### Deutsch-Jozsa Algorithm Implementation in Qiskit

This project implements the famous **Deutsch-Jozsa algorithm**, one of the first quantum algorithms to demonstrate an exponential speedup over classical computation.

The algorithm determines whether a given oracle function f:{0,1}^n → {0,1} is:
- **Constant**: outputs the same value (0 or 1) for all inputs
- **Balanced**: outputs 0 for exactly half the inputs and 1 for the other half

Using only **one query** to the oracle, the quantum algorithm solves this problem deterministically, while a classical algorithm requires up to 2^{n-1} + 1 queries in the worst case.

Features:
- n = 3 qubits (8 possible inputs)
- Two oracles: constant (always 0) and balanced (XOR of all inputs)
- Results visualized with histograms showing the clear distinction

A classic example of quantum parallelism and interference!

<img width="640" class="image" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/94e4cd8d-bab2-4a50-8eed-0059cda6e670" />
