import math


def cholesky(A, B):
    n = len(A)

    # Create lower triangular matrix L
    L = [[0.0 for _ in range(n)] for _ in range(n)]

    # Cholesky decomposition: A = L * L^T
    for i in range(n):
        for j in range(i + 1):

            sum_value = 0.0

            for k in range(j):
                sum_value += L[i][k] * L[j][k]

            if i == j:
                value = A[i][i] - sum_value

                if value <= 0:
                    raise ValueError(
                        "Matrix is not positive definite."
                    )

                L[i][j] = math.sqrt(value)

            else:
                L[i][j] = (A[i][j] - sum_value) / L[j][j]

    # Forward substitution: L * Y = B
    Y = [0.0] * n

    for i in range(n):
        sum_value = 0.0

        for j in range(i):
            sum_value += L[i][j] * Y[j]

        Y[i] = (B[i] - sum_value) / L[i][i]

    # Back substitution: L^T * X = Y
    X = [0.0] * n

    for i in range(n - 1, -1, -1):
        sum_value = 0.0

        for j in range(i + 1, n):
            sum_value += L[j][i] * X[j]

        X[i] = (Y[i] - sum_value) / L[i][i]

    return L, X


# Example system:
#
#  4x + 12y - 16z = 12
# 12x + 37y - 43z = 30
#-16x - 43y + 98z = -16

A = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
]

B = [12, 30, -16]


L, X = cholesky(A, B)


# Display L
print("L matrix:")

for row in L:
    print([round(value, 6) for value in row])


# Display solution
print("\nSolution:")

for i, value in enumerate(X, start=1):
    print(f"x{i} = {value:.2f}")
