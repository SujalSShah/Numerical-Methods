
# Doolittle's Method to Solve a System of Linear Equations

import numpy as np

# Input coefficient matrix A
A = np.array([
    [2.0, 1.0, 1.0],
    [4.0, 3.0, 3.0],
    [8.0, 7.0, 9.0]
])

# Input constant matrix B
B = np.array([4.0, 10.0, 24.0])

n = len(B)

# Initialize L and U matrices
L = np.zeros((n, n))
U = np.zeros((n, n))

# Doolittle's LU Decomposition
for i in range(n):

    # Calculate U matrix
    for j in range(i, n):
        sum1 = 0
        for k in range(i):
            sum1 += L[i][k] * U[k][j]

        U[i][j] = A[i][j] - sum1

    # Calculate L matrix
    for j in range(i, n):
        if i == j:
            L[i][i] = 1
        else:
            sum2 = 0
            for k in range(i):
                sum2 += L[j][k] * U[k][i]

            L[j][i] = (A[j][i] - sum2) / U[i][i]

# Forward Substitution: LY = B
Y = np.zeros(n)

for i in range(n):
    sum3 = 0
    for j in range(i):
        sum3 += L[i][j] * Y[j]

    Y[i] = (B[i] - sum3) / L[i][i]

# Backward Substitution: UX = Y
X = np.zeros(n)

for i in range(n - 1, -1, -1):
    sum4 = 0
    for j in range(i + 1, n):
        sum4 += U[i][j] * X[j]

    X[i] = (Y[i] - sum4) / U[i][i]

# Display results
print("Lower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

print("\nIntermediate solution Y:")
print(Y)

print("\nSolution X:")
for i in range(n):
    print(f"x{i+1} = {X[i]:.2f}")
