
import numpy as np

def sor(A, b, x0, omega, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            sum1 = 0
            sum2 = 0

            # Values already updated
            for j in range(i):
                sum1 += A[i][j] * x[j]

            # Values not yet updated
            for j in range(i + 1, n):
                sum2 += A[i][j] * x_old[j]

            # SOR formula
            x[i] = (1 - omega) * x_old[i] + \
                   (omega / A[i][i]) * (b[i] - sum1 - sum2)

        # Check convergence
        if np.linalg.norm(x - x_old, np.inf) < tol:
            print("Converged in", k + 1, "iterations")
            return x

    print("Maximum iterations reached")
    return x


# Coefficient matrix
A = np.array([
    [4, 1, 1],
    [1, 5, 1],
    [1, 1, 3]
], dtype=float)

# Right-hand side
b = np.array([7, -8, 6], dtype=float)

# Initial guess
x0 = np.array([0.0, 0.0, 0.0])

# Relaxation factor
omega = 1.25

# Solve using SOR
solution = sor(A, b, x0, omega)

print("Solution:")
for i, value in enumerate(solution):
    print(f"x{i+1} = {value:.6f}")
