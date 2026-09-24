def muller(f, x0, x1, x2, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        f2 = f(x2)

        h0 = x1 - x0
        h1 = x2 - x1

        delta0 = (f1 - f0) / h0
        delta1 = (f2 - f1) / h1

        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = f2

        # Choose the denominator with the larger magnitude
        if abs(b + (b**2 - 4*a*c)**0.5) > abs(b - (b**2 - 4*a*c)**0.5):
            denominator = b + (b**2 - 4*a*c)**0.5
        else:
            denominator = b - (b**2 - 4*a*c)**0.5

        x3 = round(x2 - (2 * c) / denominator,3)

        print(f"Iteration {i+1}: x = {x3}")

        if abs(x3 - x2) < tol:
            return x3

        x0, x1, x2 = x1, x2, x3

    return x2


# Example: Solve x^3 - x - 1 = 0
def f(x):
    return x**3 - x - 1


root = muller(f, 0, 1, 2)

print("\nRoot =", root)
