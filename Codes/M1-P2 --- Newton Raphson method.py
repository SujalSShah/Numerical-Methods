def newton_raphson(f, df, x0, n):
    print("\nIteration\t x(n)\t\t f(xn)\t\t f'(xn)\t\t x(n+1)")
    print("-"*70)

    x = x0

    for i in range(1, n+1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivative is zero. Cannot continue.")
            return

        x_new = x - (fx / dfx)

        print(f"{i}\t\t{x:.6f}\t{fx:.6f}\t{dfx:.6f}\t{x_new:.6f}")

        x = x_new

    print("\nRoot after iterations =", x)


def f(x):
    return x**2 - 3*x - 6       


def df(x):
    return 2*x - 3             


x0 = float(input("Enter initial value x0: "))
n=5


newton_raphson(f, df, x0, n)
