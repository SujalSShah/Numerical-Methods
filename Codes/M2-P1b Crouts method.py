
import numpy as np

# Coefficient matrix A
A = np.array([
    [2.0, 1.0, 1.0],
    [4.0, 3.0, 3.0],
    [8.0, 7.0, 9.0]
])

# Constant matrix B
B = np.array([4.0, 10.0, 24.0])

n = len(B)

# Initialize L and U matrices
L = np.zeros((n, n))
U = np.zeros((n, n))

# Crout's LU Decomposition
for j in range(n):

    # Calculate elements of L
    for i in range(j, n):
        sum1 = 0
        for k in range(j):
            sum1 += L[i][k] * U[k][j]

        L[i][j] = A[i][j] - sum1

    # Calculate elements of U
    for i in range(j + 1, n):
        sum2 = 0
        for k in range(j):
            sum2 += L[j][k] * U[k][i]

        U[j][i] = (A[j][i] - sum2) / L[j][j]

    # Diagonal elements of U are 1
    U[j][j] = 1

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
