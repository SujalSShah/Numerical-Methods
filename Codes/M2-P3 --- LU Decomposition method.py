def tridiagonal_lu(a, b, c, d):
    """
    Solve a tridiagonal system Ax = d using LU decomposition.

    a = lower diagonal (n-1 elements)
    b = main diagonal  (n elements)
    c = upper diagonal (n-1 elements)
    d = right-hand side (n elements)
    """

    n = len(b)

    # Make copies so original arrays are not modified
    a = a.copy()
    b = b.copy()
    c = c.copy()
    d = d.copy()

    # -------------------------
    # LU Decomposition
    # -------------------------

    for i in range(1, n):
        multiplier = a[i - 1] / b[i - 1]

        # L factor
        a[i - 1] = multiplier

        # U factor
        b[i] = b[i] - multiplier * c[i - 1]

    # -------------------------
    # Forward substitution
    # Solve Ly = d
    # -------------------------

    y = [0.0] * n

    y[0] = d[0]

    for i in range(1, n):
        y[i] = d[i] - a[i - 1] * y[i - 1]

    # -------------------------
    # Back substitution
    # Solve Ux = y
    # -------------------------

    x = [0.0] * n

    x[n - 1] = y[n - 1] / b[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - c[i] * x[i + 1]) / b[i]

    return x


# Example system:
#
#  2x1 +  x2              = 5
#   x1 + 3x2 +  x3        = 10
#       x2 + 4x3 +  x4    = 15
#           x3 + 5x4      = 10

lower = [1, 1, 1]
main  = [2, 3, 4, 5]
upper = [1, 1, 1]
rhs   = [5, 10, 15, 10]

x = tridiagonal_lu(lower, main, upper, rhs)

print("Solution:")
for i, value in enumerate(x):
    print(f"x{i+1} = {value:.6f}")
