def fixed_point(g, x0, tol=1e-6, max_iter=100):
    """
    General Iteration / Fixed Point Method

    g      : function g(x)
    x0     : initial guess
    tol    : tolerance
    max_iter: maximum number of iterations
    """

    print("Iteration\t x")

    for i in range(1, max_iter + 1):
        x1 = g(x0)

#        print(f"{i}\t\t {x1:.8f}")

        # Convergence condition
        if abs(x1 - x0) < tol:
            print("\nConverged!")
            return x1

        x0 = x1

    print("\nMethod did not converge.")
    return x0


# Example:
# Solve x^3 + x - 1 = 0
#
# Rewrite as:
# x = 1 / (x^2 + 1)

def g(x):
    return 1 / (x**2 + 1)


# Initial guess
x0 = 0.5

root = fixed_point(g, x0)

print(f"\nRoot = {root:.2f}")
