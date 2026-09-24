def chebyshev_method(f, df, ddf, x0, tol=1e-6, max_iter=100):
    x = x0

    print("Iteration\t x\t\t f(x)")

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        ddfx = ddf(x)

        # Chebyshev formula
        x_new = x - (fx / dfx) - (ddfx * fx**2) / (2 * dfx**3)

        print(f"{i+1}\t\t {x_new:.8f}\t {f(x_new):.8f}")

        # Stopping condition
        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x


# Example:
# Solve x^3 - x - 2 = 0

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def ddf(x):
    return 6*x


root = chebyshev_method(f, df, ddf, x0=1.5)
rroot=round(root,2)
print("\nAn approximate root =", rroot)
